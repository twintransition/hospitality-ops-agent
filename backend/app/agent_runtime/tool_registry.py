"""Tool registry for agent capabilities.

Agents should interact with business capabilities through tools,
not directly through database access.
"""

from typing import Callable, Dict


class ToolRegistry:
    """Registry of capabilities exposed to agents."""

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, function: Callable):
        self._tools[name] = function

    def get(self, name: str) -> Callable:
        return self._tools.get(name)

    def available_tools(self):
        return list(self._tools.keys())

    def describe(self):
        return {
            "tools": self.available_tools()
        }


registry = ToolRegistry()
