"""Scenario evaluation runner.

Runs operational scenarios through the agent pipeline and validates
expected intent/workflow outcomes.
"""

import json
from pathlib import Path

from app.agent_runtime.execution import execute_agent_request


SCENARIO_DIR = Path(__file__).parent / "scenarios"


def load_scenarios():
    return list(SCENARIO_DIR.glob("*.json"))


def evaluate_scenario(path):
    scenario = json.loads(path.read_text())

    result = execute_agent_request(
        message=scenario["input"],
        guest_id=scenario.get("guest_id"),
        reservation_id=scenario.get("reservation_id"),
    )

    intent_ok = (
        result.state.intent == scenario.get("expected_intent")
    )

    workflow_ok = (
        result.state.workflow == scenario.get("expected_workflow")
        if scenario.get("expected_workflow")
        else True
    )

    return {
        "scenario": path.name,
        "intent_expected": scenario.get("expected_intent"),
        "intent_actual": result.state.intent,
        "workflow_expected": scenario.get("expected_workflow"),
        "workflow_actual": result.state.workflow,
        "passed": intent_ok and workflow_ok,
        "trace": result.state.trace,
    }


def run():
    return [evaluate_scenario(path) for path in load_scenarios()]


if __name__ == "__main__":
    for result in run():
        print(json.dumps(result, indent=2))
