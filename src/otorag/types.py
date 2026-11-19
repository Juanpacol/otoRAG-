"""Tipos de datos compartidos entre capas."""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Chunk:
    id: str
    text: str
    source: str          # documento de origen
    page: int | None     # para citar
    version: str         # versión del índice o del documento
    language: str        # "es" | "en"
    metadata: dict = field(default_factory=dict)


@dataclass(frozen=True)
class Hit:
    chunk: Chunk
    score: float


@dataclass(frozen=True)
class Answer:
    text: str
    citations: list[Chunk]
    grounded: bool       # False => "no hay evidencia en las guías"
