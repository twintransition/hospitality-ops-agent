"""Workflow API endpoints."""

from fastapi import APIRouter

from app.workflows.late_checkin_workflow import evaluate_late_checkin

router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.post("/late-checkin")
def late_checkin(payload: dict):
    """Evaluate a late check-in request using MVP business rules."""
    reservation = payload.get("reservation", {})
    policy = payload.get("policy", {})

    result = evaluate_late_checkin(reservation, policy)

    return {
        "workflow": "late_checkin",
        "result": result,
    }
