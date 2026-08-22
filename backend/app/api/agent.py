"""Agent execution API.

Exposes the controlled agent runtime without coupling the API layer
with model providers.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.agent_runtime.execution import run_agent

router = APIRouter(prefix="/agent", tags=["agent"])


class AgentRequest(BaseModel):
    message: str
    guest_id: str | None = None
    reservation_id: str | None = None


@router.post("/run")
def execute_agent(request: AgentRequest):
    return run_agent(
        message=request.message,
        guest_id=request.guest_id,
        reservation_id=request.reservation_id,
    )
