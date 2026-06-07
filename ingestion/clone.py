"""把"仓库来源"统一成一个本地目录路径。

来源可以是:
  - 本地目录(已经 clone 好,或离线部署时直接给路径)→ 原样返回
  - git URL → 浅克隆(depth=1)到工作目录

离线部署机上通常走"本地目录"分支;开发机上可以直接 clone。
"""

from __future__ import annotations

import os
from pathlib import Path

from git import Repo


def prepare_repo(source: str, workdir: str = ".cache/repos") -> Path:
    """返回可供解析的本地仓库根目录。

    Args:
        source: 本地路径或 git URL。
        workdir: clone 的落地目录(仅 URL 时使用)。
    """
    # 本地已存在的目录:直接用,不联网。
    p = Path(source).expanduser()
    if p.exists() and p.is_dir():
        return p.resolve()

    # 否则按 URL 处理,浅克隆。
    if not _looks_like_url(source):
        raise FileNotFoundError(
            f"来源既不是已存在的目录,也不像 git URL: {source!r}"
        )

    name = _repo_name_from_url(source)
    dest = Path(workdir).expanduser().resolve() / name
    if dest.exists():
        # 已克隆过,复用,避免重复联网(契合离线/弱网场景)。
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)
    Repo.clone_from(source, dest, depth=1)
    return dest


def _looks_like_url(s: str) -> bool:
    return s.startswith(("http://", "https://", "git@", "ssh://")) or s.endswith(".git")


def _repo_name_from_url(url: str) -> str:
    tail = url.rstrip("/").split("/")[-1]
    if tail.endswith(".git"):
        tail = tail[:-4]
    return tail or "repo"
