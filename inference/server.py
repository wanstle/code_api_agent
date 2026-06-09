"""llama-server 生命周期管理:启动 / 停止 / 重启 + 健康检查。

用于"安全闭环":长批量生成时,显存涨高就**重启 server 释放显存**再续跑。
重启是释放 llama.cpp 进程内 KV/碎片显存的唯一可靠手段。
"""

from __future__ import annotations

import os
import subprocess
import time
import urllib.request
from pathlib import Path


class LlamaServer:
    def __init__(
        self,
        script: str = "scripts/serve_llama_prebuilt_vulkan.sh",
        port: int = 8080,
        env: dict | None = None,
    ) -> None:
        self.script = str(Path(script).resolve())
        self.port = port
        self.env = {**os.environ, "PORT": str(port), **(env or {})}
        self.proc: subprocess.Popen | None = None

    @property
    def health_url(self) -> str:
        return f"http://127.0.0.1:{self.port}/health"

    def healthy(self, timeout: float = 2.0) -> bool:
        try:
            with urllib.request.urlopen(self.health_url, timeout=timeout) as r:
                return b'"status":"ok"' in r.read()
        except Exception:
            return False

    def start(self, wait_s: int = 120, log_path: str = ".cache/llama_server.log") -> None:
        """启动并等待健康(脚本自身会先清残留实例)。"""
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        logf = open(log_path, "ab")
        # 脚本里用了 exec,故该子进程最终就是 llama-server 本体。
        self.proc = subprocess.Popen(
            ["bash", self.script], env=self.env, stdout=logf, stderr=logf
        )
        for _ in range(wait_s):
            if self.healthy():
                return
            time.sleep(1)
        raise RuntimeError(f"llama-server 启动超时({wait_s}s),见 {log_path}")

    def stop(self) -> None:
        """停止并确保进程释放(连带兜底 pkill,确保显存归还)。"""
        if self.proc is not None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                self.proc.kill()
            self.proc = None
        # 兜底:清理任何残留实例(防显存不释放)
        subprocess.run(["pkill", "-x", "llama-server"], capture_output=True)
        time.sleep(2)

    def restart(self, **kw) -> None:
        self.stop()
        self.start(**kw)

    # 支持 with 语法,确保退出时一定停掉、释放显存
    def __enter__(self) -> "LlamaServer":
        self.start()
        return self

    def __exit__(self, *exc) -> None:
        self.stop()
