"""Graph node for response generation."""

from app.agents.response_agent import build_response


def run_response_node(state):
    state["final_response"] = build_response(state)
    state.setdefault("trace", []).append({
        "component": "response_node",
        "event": "response_generated"
    })
    return state
