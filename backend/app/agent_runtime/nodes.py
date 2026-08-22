"""Agent graph nodes.

Nodes are intentionally separated from orchestration so each capability can be
replaced, evaluated, or deployed independently.
"""

from app.agents.intent_agent import IntentAgent


class IntentNode:
    def __init__(self):
        self.agent = IntentAgent()

    def run(self, state):
        result = self.agent.classify(state.user_message)
        state.intent = result.intent
        state.confidence = result.confidence
        state.trace.append({
            "node": "intent",
            "intent": result.intent,
            "confidence": result.confidence,
        })
        return state


class WorkflowNode:
    def run(self, state, workflow_router):
        workflow = workflow_router.route(state.intent)
        state.trace.append({"node": "workflow_router", "workflow": workflow})
        state.workflow = workflow
        return state
