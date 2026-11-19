# syntax=docker/dockerfile:1
# Etapa 1: instala dependencias en un venv (no deja cachés en la imagen final)
FROM python:3.11-slim AS builder
ARG REQS=api
WORKDIR /build
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements/${REQS}.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: imagen final mínima, solo el venv y el código
FROM python:3.11-slim
ENV PATH="/opt/venv/bin:$PATH" PYTHONUNBUFFERED=1 PYTHONPATH=/app/src
COPY --from=builder /opt/venv /opt/venv
WORKDIR /app
COPY src ./src
# Modelos y datos van en volumen, no en la imagen
VOLUME ["/data"]
EXPOSE 8000
CMD ["uvicorn", "otorag.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
