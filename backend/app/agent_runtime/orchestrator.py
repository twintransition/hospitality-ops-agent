"""
Agent execution orchestrator.

This layer intentionally contains no LLM calls yet.
It coordinates state, tools, workflows, and traces so that
future model integrations can be added without redesigning
business logic.
"""

from .state import AgentState
from .trace import add_trace


class AgentOrchestrator:
    """Coordinates agent execution lifecycle."""

    def run(self, state: AgentState) -> AgentState:
        add_trace(
            state,
            component="orchestrator",
            event="workflow_started",
            data={"conversation_id": state.conversation_id},
        )

        # Future stages:
        # 1. Intent agent
        # 2. Tool selection
        # 3. Workflow execution
        # 4. Response generation

        add_trace(
            state,
            component="orchestrator",
            event="workflow_completed",
            data={"status": "ready_for_agent_steps"},
        )

        return state
