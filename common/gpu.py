"""内存看门狗:长批量任务里防止把(显存/统一内存)逼到 OOM / DeviceLost。

按平台自动选内存来源(从准到糙):
  1. 开发机 NVIDIA 独显 → nvidia-smi 查显存空闲。
  2. **AMD APU(Strix Halo)→ 读 /sys/class/drm/cardN/device/mem_info_*(VRAM+GTT)**。
     这是关键:统一内存下模型进的是 GPU 的 VRAM 划分区,`/proc/meminfo` 测不准,
     必须读 GPU 自己的 vram/gtt 占用。
  3. 兜底 → /proc/meminfo 系统可用内存。
都拿不到则降级"不检查",不影响运行。
"""

from __future__ import annotations

import glob
import shutil
import subprocess
from typing import Optional


class MemoryLowError(RuntimeError):
    """空闲内存低于安全阈值时抛出,用于提前优雅中止 + 触发重启释放。"""


def mem_source() -> str:
    if shutil.which("nvidia-smi") is not None:
        return "nvidia"
    if _amd_card_dir() is not None:
        return "amd-gpu"
    return "system"


def free_mem_mib() -> Optional[int]:
    """返回空闲内存(MiB);拿不到时 None(视为不检查)。"""
    if shutil.which("nvidia-smi") is not None:
        v = _nvidia_free_mib()
        if v is not None:
            return v
    v = _amd_gpu_free_mib()
    if v is not None:
        return v
    return _meminfo_available()


def check_memory(min_free_mib: int = 2000) -> None:
    """空闲内存低于阈值则抛 MemoryLowError;无法检测时直接放行。"""
    free = free_mem_mib()
    if free is not None and free < min_free_mib:
        raise MemoryLowError(
            f"空闲内存仅 {free} MiB(< {min_free_mib},来源={mem_source()}),为防 OOM 提前中止"
        )


# ---------- NVIDIA ----------
def _nvidia_free_mib() -> Optional[int]:
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=memory.free", "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
        vals = [int(x) for x in out.splitlines() if x.strip().isdigit()]
        return min(vals) if vals else None
    except (subprocess.SubprocessError, ValueError):
        return None


# ---------- AMD APU(VRAM + GTT 经 sysfs)----------
def _amd_card_dir() -> Optional[str]:
    for d in sorted(glob.glob("/sys/class/drm/card*/device")):
        try:
            with open(f"{d}/mem_info_vram_total"):
                return d
        except OSError:
            continue
    return None


def _amd_gpu_free_mib() -> Optional[int]:
    d = _amd_card_dir()
    if d is None:
        return None

    def rd(name: str) -> Optional[int]:
        try:
            with open(f"{d}/mem_info_{name}") as f:
                return int(f.read().strip())
        except (OSError, ValueError):
            return None

    vt, vu = rd("vram_total"), rd("vram_used")
    gt, gu = rd("gtt_total"), rd("gtt_used")
    if vt is None or vu is None:
        return None
    free = (vt - vu) + ((gt - gu) if (gt is not None and gu is not None) else 0)
    return free // (1024 * 1024)


# ---------- 兜底:系统可用内存 ----------
def _meminfo_available() -> Optional[int]:
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1]) // 1024
    except (OSError, ValueError, IndexError):
        return None
    return None
