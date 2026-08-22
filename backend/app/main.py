from fastapi import FastAPI

app = FastAPI(
    title="Hospitality Operations Agent",
    version="0.1.0"
)


@app.get("/")
def health_check():
    return {
        "service": "hospitality-ops-agent",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
