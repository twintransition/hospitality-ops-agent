"""Housekeeping request workflow."""


def execute_housekeeping(context: dict) -> dict:
    issue_type = context.get("issue_type", "general")
    priority = "high" if issue_type in {"maintenance", "urgent"} else "normal"

    return {
        "workflow": "housekeeping",
        "decision": "task_created",
        "priority": priority,
        "required_actions": ["create_housekeeping_task"],
    }
