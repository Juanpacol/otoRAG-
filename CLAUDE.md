# CLAUDE.md — OtoRAG

Contexto del proyecto para Claude Code. Mantener este archivo corto y actualizado.

## Qué es
**OtoRAG**: asistente agéntico con RAG híbrido sobre guías clínicas de **vértigo** (otoneurología).
Responde con **cita de fuente y página**, y dice "no hay evidencia en las guías" cuando no la hay.
Proyecto del curso de Inteligencia Artificial (ING01200), tema: Agentes / RAG.

## Alcance y límites (no negociables)
- Uso **educativo** (estudiantes de medicina/fisioterapia). **No diagnostica ni receta.**
- Toda respuesta incluye aviso de que no reemplaza a un profesional de salud.
- Solo se responde con lo recuperado de las fuentes indexadas. Si no hay evidencia, se dice.
- Solo fuentes oficiales/abiertas, con licencia revisada antes de indexar.

## Patologías cubiertas
VPPB, enfermedad de Ménière, neuritis vestibular, causas centrales (señales de alarma, diagnóstico diferencial). Migraña vestibular: pendiente de fuente.

## Arquitectura (capas)
1. Ingesta: parseo de PDFs, limpieza, metadatos (fuente, página, versión, idioma).
2. Chunking: recursivo, 300–500 tokens, 10–15% overlap, con contexto por chunk (contextual retrieval).
3. Indexado: vectores + índice BM25.
4. Recuperación: híbrida (BM25 + densa, fusión RRF) + reranker cross-encoder.
5. Generación: respuesta solo con contexto recuperado, con citas.
6. Agente: decide cuándo recuperar, reformula la consulta, verifica suficiencia de evidencia.
7. Evaluación: set de preguntas con respuesta verificada; métricas de recuperación y faithfulness.
8. Observabilidad: trazas por paso, latencia y costo.

## Principios de escalabilidad
- Dos caminos separados: **ingesta** (offline, idempotente) y **consulta** (API sin estado).
- Cada capa se define por una interfaz en `src/otorag/interfaces.py`; el stack se elige en `src/otorag/config/settings.yaml`. No acoplar el agente a una librería concreta.
- Índice **versionado**: cambiar de versión solo si la nueva pasa la evaluación.
- No sobreconstruir: sin colas distribuidas ni réplicas para ~10 documentos. Diseñar preparado, demostrar pequeño.

## Estructura del repo
```
src/otorag/  ingestion/ retrieval/ generation/ agent/ api/ evaluation/ config/
             interfaces.py (contratos)  types.py (Chunk, Hit, Answer)
docs/sources.md   data/raw (PDFs, ignorados por git)   data/eval (preguntas)   tests/
```

## Decisiones de stack
Estado: **propuesto, sin confirmar**. Cambiar aquí cuando se decida.
- Lenguaje: Python 3.11+ (el `python3` del sistema es 3.9; usar `python3.11` o un venv).
- Vector store: pgvector o Qdrant (decidir).
- BM25: `rank_bm25` o equivalente.
- Embeddings: multilingüe (consultas en español sobre documentos en inglés).
- Reranker: BGE (local) o Cohere (hosted, revisar límites gratuitos).
- Agente: LangGraph.
- Evaluación: RAGAS o DeepEval.
- Trazas: Langfuse.
- Extra opcional: servidor MCP que exponga la búsqueda.
- LLM/API: pendiente de confirmar qué permite el profesor.

## Fuentes candidatas (verificar disponibilidad, licencia y fecha)
- AAO-HNS: guía VPPB (2008) y guía Ménière (2020).
- Revisión 2026 sobre trastornos vestibulares (Springer): revisión, no guía formal.
- Guía de vértigo en maternoinfantil.gov.co: emisor y fecha sin confirmar.
- Guía VPPB del Colegio de Médicos de Madrid; guía técnica VPPB de Perú.
- NHS: manejo del vértigo en atención primaria.
- Huecos: guía abierta de neuritis vestibular; guía oficial colombiana.

## Reglas de trabajo
- Reutilizar bases open source si ayudan, **citando el repo origen** y revisando su licencia. Candidatos: `Umanagalla27/p1-production-rag` (RAG + evals + trazas), `Coregenion-WQ/rag-research-agent-template` o `GiovanniPasq/agentic-rag-for-dummies` (agente). No auditados: correr el ejemplo antes de adaptar.
- Primero línea base, luego mejoras; medir cada cambio contra el mismo set de preguntas.
- Cambios pequeños y verificables. No añadir funciones no pedidas.
- No commitear PDFs con licencia dudosa, claves de API ni `.env`.
- Revisión médica del set de preguntas: idealmente por alguien con formación en salud.

## Pendientes
- [ ] Confirmar con el profesor: tema, entregables, rúbrica, fecha y API permitida.
- [ ] Decidir stack final.
- [ ] Descargar y revisar fuentes (texto legible, licencia).
- [ ] Crear estructura del repo y entorno.
- [ ] Línea base RAG, luego híbrido + reranker.
- [ ] Set de 30–50 preguntas y evaluación.
- [ ] Capa de agente.
- [ ] Informe y exposición (exposiciones desde el 23 nov).
