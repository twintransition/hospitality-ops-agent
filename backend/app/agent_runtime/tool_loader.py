"""Loads business tools into the agent runtime."""

from app.agent_runtime.tool_registry import registry
from app.tools.reservation_tool import lookup_reservation
from app.tools.policy_tool import retrieve_policy
from app.tools.action_tool import record_agent_action


def load_tools():
    registry.register("lookup_reservation", lookup_reservation)
    registry.register("retrieve_policy", retrieve_policy)
    registry.register("record_agent_action", record_agent_action)
    return registry
