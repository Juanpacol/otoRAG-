"""Contratos de cada capa. El stack concreto se elige por configuración."""
from typing import Protocol

from otorag.types import Answer, Chunk, Hit


class VectorStore(Protocol):
    def upsert(self, chunks: list[Chunk]) -> None: ...
    def search_dense(self, query: str, k: int) -> list[Hit]: ...
    def search_keyword(self, query: str, k: int) -> list[Hit]: ...


class Retriever(Protocol):
    def retrieve(self, query: str, k: int) -> list[Hit]: ...


class Reranker(Protocol):
    def rerank(self, query: str, hits: list[Hit], top_n: int) -> list[Hit]: ...


class Generator(Protocol):
    def generate(self, query: str, context: list[Hit]) -> Answer: ...
