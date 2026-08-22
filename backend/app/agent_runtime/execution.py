"""Agent execution pipeline.

Coordinates interpretation and workflow routing while keeping business logic
outside the model layer.
"""

from .state import AgentState
from .trace import add_trace_event
from app.agents.intent_agent import classify_intent


def execute_agent_request(message: str, workflow_router=None):
    """Run one agent request through interpretation and optional routing."""

    state = AgentState(user_message=message)

    add_trace_event(
        state,
        "agent_runtime",
        "request_received",
        {"message": message},
    )

    intent = classify_intent(message)
    state.intent = intent.intent
    state.confidence = intent.confidence
    state.entities = getattr(intent, "entities", {})

    add_trace_event(
        state,
        "intent_agent",
        "intent_classified",
        {
            "intent": state.intent,
            "confidence": state.confidence,
        },
    )

    if workflow_router:
        result = workflow_router(state)
        state.final_response = result

        add_trace_event(
            state,
            "workflow_router",
            "workflow_completed",
            {"result": result},
        )

    return state
