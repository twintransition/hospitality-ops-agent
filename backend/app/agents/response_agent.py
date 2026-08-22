"""Response agent boundary.

This module converts grounded workflow outcomes into guest-facing responses.
The implementation is intentionally provider-agnostic; LLM generation will be
introduced through the model provider layer.
"""

from typing import Any, Dict


def build_response(state: Dict[str, Any]) -> str:
    """Create a safe response from workflow state.

    The response layer should consume verified workflow outputs rather than
    inventing operational decisions.
    """
    if state.get("workflow_result"):
        return str(state["workflow_result"])

    return "Your request has been received and is being processed."
