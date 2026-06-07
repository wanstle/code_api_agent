"""fastembed embedding 封装(CPU,ONNX)。

放 CPU 跑:全机只有一块 iGPU 要留给 LLM(见 README 选型),索引是一次性开销。
首次使用会从 HF 拉取 ONNX 模型到本地缓存;离线机需提前把缓存拷过去。
"""

from __future__ import annotations

import os
from typing import Iterable

from fastembed import TextEmbedding

DEFAULT_MODEL = os.environ.get("EMBED_MODEL", "BAAI/bge-small-en-v1.5")


class Embedder:
    def __init__(self, model_name: str = DEFAULT_MODEL) -> None:
        self.model_name = model_name
        self._model = TextEmbedding(model_name)
        self._dim: int | None = None

    @property
    def dim(self) -> int:
        if self._dim is None:
            self._dim = len(next(iter(self._model.embed(["x"]))))
        return self._dim

    def embed(self, texts: Iterable[str], batch_size: int = 64) -> list[list[float]]:
        """返回与输入等长的向量列表。"""
        return [v.tolist() for v in self._model.embed(list(texts), batch_size=batch_size)]

    def embed_one(self, text: str) -> list[float]:
        return next(iter(self._model.embed([text]))).tolist()
