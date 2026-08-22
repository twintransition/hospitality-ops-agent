"""Stateful agent execution graph.

This provides a lightweight LangGraph-style structure while keeping the project
framework independent.
"""

from app.agent_runtime.nodes import IntentNode, WorkflowNode
from app.agent_runtime.transitions import next_step


class HospitalityAgentGraph:
    def __init__(self, workflow_router):
        self.intent_node = IntentNode()
        self.workflow_node = WorkflowNode()
        self.workflow_router = workflow_router

    def run(self, state):
        state = self.intent_node.run(state)
        state = self.workflow_node.run(state, self.workflow_router)
        state.trace.append({
            "node": "transition",
            "next": next_step(state.intent),
        })
        return state
