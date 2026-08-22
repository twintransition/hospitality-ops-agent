"""Hospitality Operations Agent API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import workflows

app = FastAPI(
    title="Hospitality Operations Agent",
    description="MVP AI operations workflow platform for hospitality use cases.",
    version="0.1.0",
)

# Frontend development server support.
# Restrict further during production deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
