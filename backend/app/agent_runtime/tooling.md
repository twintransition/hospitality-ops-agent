# Agent Tool Architecture

The agent runtime accesses business capabilities through tools.

Flow:

```
Agent
  |
  v
Tool Registry
  |
  v
Business Tool
  |
  v
Service Layer
  |
  v
Database
```

Initial tools:

- lookup_reservation
- retrieve_policy
- record_agent_action

The agent should never directly execute SQL or manipulate persistence objects.
