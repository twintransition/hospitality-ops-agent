"""Lightweight scenario evaluation runner."""

import json
from pathlib import Path


def load_scenarios():
    scenario_dir = Path(__file__).parent / "scenarios"
    return list(scenario_dir.glob("*.json"))


def run():
    results = []
    for scenario in load_scenarios():
        data = json.loads(scenario.read_text())
        results.append({
            "scenario": scenario.name,
            "expected_intent": data.get("expected_intent"),
            "status": "ready_for_execution",
        })
    return results


if __name__ == "__main__":
    for result in run():
        print(result)
