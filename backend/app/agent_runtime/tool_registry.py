"""Tool registry for agent capabilities.

Agents should interact with business capabilities through tools,
not directly through database access.
"""


class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, name, function):
        self._tools[name] = function

    def get(self, name):
        return self._tools.get(name)

    def available_tools(self):
        return list(self._tools.keys())
