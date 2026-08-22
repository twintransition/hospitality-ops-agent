"""Central workflow registry."""

from .late_checkin_workflow import run_late_checkin_workflow
from .cancellation_workflow import run_cancellation_workflow
from .room_upgrade_workflow import run_room_upgrade_workflow
from .housekeeping_workflow import run_housekeeping_workflow

WORKFLOWS = {
    "late_checkin": run_late_checkin_workflow,
    "cancellation": run_cancellation_workflow,
    "room_upgrade": run_room_upgrade_workflow,
    "housekeeping": run_housekeeping_workflow,
}


def get_workflow(intent: str):
    return WORKFLOWS.get(intent)
