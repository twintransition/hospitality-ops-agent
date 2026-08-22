# Agent Runtime

The agent runtime is the control layer around future LLM components.

Design principle:

```
Model + Harness = Agent System
```

The runtime manages:

- state
- execution flow
- tools
- traces
- evaluation hooks

Current implementation intentionally has no external model dependency.

Planned evolution:

```
User request
    |
    v
Intent Router Agent
    |
    v
Workflow Controller
    |
    +--> Reservation tools
    |
    +--> SOP retrieval
    |
    v
Action execution
    |
    v
Trace + evaluation
```
