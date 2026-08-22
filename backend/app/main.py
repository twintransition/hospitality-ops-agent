"""Hospitality Operations Agent API."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import workflows, actions
from app.database.startup import initialize_application_database


@asynccontextmanager
def lifespan(app: FastAPI):
    """Initialize local operational database on application startup."""
    initialize_application_database()
    yield


app = FastAPI(
    title="Hospitality Operations Agent",
    description="MVP AI operations workflow platform for hospitality use cases.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workflows.router)
app.include_router(actions.router)


@app.get("/")
def root():
    return {
        "project": "hospitality-ops-agent",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
