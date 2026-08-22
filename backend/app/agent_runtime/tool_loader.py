"""Loads business tools into the agent runtime."""

from app.agent_runtime.tool_registry import registry
from app.tools.reservation_tool import lookup_reservation
from app.tools.policy_tool import retrieve_policy
from app.tools.action_tool import record_agent_action
from app.tools.cancellation_tool import check_cancellation_policy, request_cancellation
from app.tools.upgrade_tool import check_upgrade_availability, create_upgrade_request
from app.tools.housekeeping_tool import create_housekeeping_task, check_task_status


def load_tools():
    registry.register("lookup_reservation", lookup_reservation)
    registry.register("retrieve_policy", retrieve_policy)
    registry.register("record_agent_action", record_agent_action)

    registry.register("check_cancellation_policy", check_cancellation_policy)
    registry.register("request_cancellation", request_cancellation)

    registry.register("check_upgrade_availability", check_upgrade_availability)
    registry.register("create_upgrade_request", create_upgrade_request)

    registry.register("create_housekeeping_task", create_housekeeping_task)
    registry.register("check_task_status", check_task_status)

    return registry
