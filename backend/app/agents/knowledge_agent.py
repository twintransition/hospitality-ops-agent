from app.agent_runtime.state import AgentState
from app.knowledge.retrieval_service import KnowledgeRetrievalService


retrieval_service = KnowledgeRetrievalService()


def run_knowledge_agent(state: AgentState) -> AgentState:
    query = state.user_message
    context = retrieval_service.retrieve(query)
    state.retrieved_context = context

    if hasattr(state, "trace"):
        state.trace.append({
            "component": "knowledge_agent",
            "event": "context_retrieved",
            "source": "knowledge_retrieval_service"
        })

    return state
