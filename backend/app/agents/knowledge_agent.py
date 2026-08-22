from app.agent_runtime.state import AgentState
from app.knowledge.retriever import retrieve


def run_knowledge_agent(state: AgentState) -> AgentState:
    query = state.user_message
    context = retrieve(query)
    state.retrieved_context = context

    if hasattr(state, "trace"):
        state.trace.append({
            "component": "knowledge_agent",
            "event": "context_retrieved"
        })

    return state
