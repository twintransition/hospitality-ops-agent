"""Agent runtime state definitions.

The state object is intentionally framework-independent.
It can later map to LangGraph or another orchestration framework.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentState:
    conversation_id: Optional[str] = None
    guest_id: Optional[str] = None
    reservation_id: Optional[str] = None
    user_message: str = ""
    intent: Optional[str] = None
    confidence: float = 0.0
    retrieved_context: List[Dict[str, Any]] = field(default_factory=list)
    tool_results: Dict[str, Any] = field(default_factory=dict)
    actions: List[str] = field(default_factory=list)
    final_response: Optional[str] = None
    trace: List[Dict[str, Any]] = field(default_factory=list)
