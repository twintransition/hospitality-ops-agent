"""Hospitality Operations Agent API."""

from fastapi import FastAPI

from app.api import workflows

app = FastAPI(
    title="Hospitality Operations Agent",
    description="MVP AI operations workflow platform for hospitality use cases.",
    version="0.1.0",
)

app.include_router(workflows.router)


@app.get("/")
def root():
    return {
        "project": "hospitality-ops-agent",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
