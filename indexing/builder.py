"""把一个仓库构建成可检索的索引。

流程:clone/定位 → 扫描 → tree-sitter 解析 → 代码感知分块 → fastembed 向量化
      → 写入 Chroma(向量索引)+ SQLite(符号索引),并存一份 meta.json。
索引落在 .cache/index/<repo_name>/。
"""

from __future__ import annotations

import json
from pathlib import Path

from common.models import RepoMap
from ingestion.clone import prepare_repo
from ingestion.filetree import scan_files
from ingestion.parse import parse_repo
from indexing.chunk import chunk_repo
from indexing.embed import Embedder
from indexing.symbol_index import SymbolIndex
from indexing.vector_store import VectorStore

INDEX_BASE = ".cache/index"


def index_dir_for(name: str) -> Path:
    return Path(INDEX_BASE) / name


def build_index(source: str, progress=print) -> Path:
    root = prepare_repo(source)
    progress(f"定位仓库: {root}")

    files = scan_files(root)
    repo: RepoMap = parse_repo(root, files)
    progress(f"解析完成: {repo.num_files} 文件 / {repo.num_symbols} 符号")

    chunks = chunk_repo(repo)
    progress(f"代码感知分块: {len(chunks)} chunks")

    idir = index_dir_for(repo.name)
    idir.mkdir(parents=True, exist_ok=True)

    # 向量索引
    embedder = Embedder()
    progress(f"embedding({embedder.model_name}, CPU) …")
    vectors = embedder.embed([c.embed_text() for c in chunks])
    vs = VectorStore(str(idir / "chroma"))
    vs.add(chunks, vectors)
    progress(f"向量索引写入: {vs.count()} 条")

    # 符号索引
    si = SymbolIndex(str(idir / "symbols.db"))
    n_sym = si.build(repo)
    si.close()
    progress(f"符号索引写入: {n_sym} 条")

    meta = {
        "name": repo.name,
        "root": repo.root,
        "embed_model": embedder.model_name,
        "dim": embedder.dim,
        "num_files": repo.num_files,
        "num_chunks": len(chunks),
        "num_symbols": n_sym,
        "languages": repo.language_breakdown(),
        # 紧凑文件清单,供 D3 构建"仓库概览前缀"(按符号数排序便于截断取重点)
        "files": sorted(
            [
                {"path": f.path, "lang": f.language, "symbols": len(f.symbols), "lines": f.lines}
                for f in repo.files
            ],
            key=lambda d: -d["symbols"],
        ),
    }
    (idir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), "utf-8")
    progress(f"索引完成 → {idir}")
    return idir
