"""Chroma 向量索引封装。

我们用 fastembed 自己算向量后传进来(embeddings=...),不依赖 Chroma 内置 EF,
这样 embedding 模型可控、可换。底层 Chroma 用 SQLite 持久化。
"""

from __future__ import annotations

from pathlib import Path

import chromadb

from indexing.chunk import CodeChunk


class VectorStore:
    def __init__(self, persist_dir: str, name: str = "code") -> None:
        Path(persist_dir).mkdir(parents=True, exist_ok=True)
        self._client = chromadb.PersistentClient(path=persist_dir)
        # cosine 距离更适合归一化文本向量。
        self._col = self._client.get_or_create_collection(
            name=name, metadata={"hnsw:space": "cosine"}
        )

    def add(self, chunks: list[CodeChunk], embeddings: list[list[float]]) -> None:
        for i in range(0, len(chunks), 1000):  # Chroma 单批有上限,分批写
            batch = chunks[i : i + 1000]
            embs = embeddings[i : i + 1000]
            self._col.add(
                ids=[c.id for c in batch],
                embeddings=embs,
                documents=[c.text for c in batch],
                metadatas=[
                    {
                        "file": c.file,
                        "name": c.name,
                        "kind": c.kind,
                        "language": c.language,
                        "parent": c.parent,
                        "qualified_name": c.qualified_name(),
                        "signature": c.signature,
                        "start_line": c.start_line,
                        "end_line": c.end_line,
                    }
                    for c in batch
                ],
            )

    def query(self, query_embedding: list[float], k: int = 8) -> list[dict]:
        res = self._col.query(query_embeddings=[query_embedding], n_results=k)
        out: list[dict] = []
        ids = res.get("ids", [[]])[0]
        docs = res.get("documents", [[]])[0]
        metas = res.get("metadatas", [[]])[0]
        dists = res.get("distances", [[]])[0]
        for cid, doc, meta, dist in zip(ids, docs, metas, dists):
            out.append(
                {
                    "id": cid,
                    "text": doc,
                    "score": 1.0 - float(dist),  # cosine 距离 → 相似度
                    **meta,
                }
            )
        return out

    def count(self) -> int:
        return self._col.count()
