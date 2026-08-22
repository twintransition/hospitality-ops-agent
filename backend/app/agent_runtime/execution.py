"""Agent execution pipeline.

Coordinates interpretation and workflow routing while keeping business logic
outside the model layer.
"""

from .state import AgentState
from .trace import add_trace_event
from app.agents.intent_agent import classify_intent


def execute_agent_request(message: str, workflow_router=None):
    state = AgentState(user_message=message)

    intent = classify_intent(message)
    state.intent = intent.intent
    state.confidence = intent.confidence

    add_trace_event(
        state,
        "intent_agent",
        "intent_classified",
        {"intent": state.intent, "confidence": state.confidence},
    )

    if workflow_router:
        result = workflow_router(state)
        state.final_response = result

    return state
