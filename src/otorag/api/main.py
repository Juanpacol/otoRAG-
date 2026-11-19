from fastapi import FastAPI

app = FastAPI(title="OtoRAG")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
