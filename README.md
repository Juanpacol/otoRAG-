# OtoRAG

Asistente agéntico con RAG híbrido para consultar guías clínicas de **vértigo**, con respuestas citadas y evaluación automática.

> **Aviso:** proyecto educativo. No diagnostica, no receta y no reemplaza a un profesional de la salud.

## Estado
En planeación. Aún no hay código. Ver [CLAUDE.md](CLAUDE.md) para decisiones y pendientes.

## Qué hará
- Responder preguntas sobre VPPB, enfermedad de Ménière, neuritis vestibular y causas centrales.
- Citar la guía y la página de cada afirmación.
- Decir "no hay evidencia en las guías" cuando no la haya.
- Aceptar consultas en español sobre documentos en español e inglés.

## Cómo funciona (diseño)
```
PDFs de guías → ingesta y chunking → índice (BM25 + vectores)
consulta → agente → recuperación híbrida (RRF) → reranker → respuesta con citas
                         ↑ reformula / verifica evidencia
evaluación (preguntas con respuesta verificada) + trazas de cada paso
```

## Stack propuesto
Python · pgvector o Qdrant · BM25 · embeddings multilingües · reranker BGE o Cohere · LangGraph · RAGAS o DeepEval · Langfuse.
Sujeto a cambios.

## Fuentes
Guías y revisiones abiertas sobre vértigo (AAO-HNS, NHS, guías en español y otras). La lista, con licencias y fechas verificadas, estará en `docs/sources.md`.

## Hoja de ruta
1. Línea base: RAG simple con citas.
2. Búsqueda híbrida y reranker.
3. Set de preguntas y evaluación; tabla comparando cada variante.
4. Capa de agente.
5. Demo, informe y exposición.

## Créditos
Se reutilizarán ideas o código de repositorios open source; cada uno se citará aquí con su licencia.

## Licencia
Por definir.
