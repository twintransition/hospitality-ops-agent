# AI Agent Architecture

## Design goal

This project is not designed as a chatbot. The goal is an operational AI system that helps hospitality teams complete workflows reliably.

The core principle:

```
User request
    ↓
Agent interpretation
    ↓
Business workflow
    ↓
Tools and data access
    ↓
Action
    ↓
Audit trail
```

## Current MVP foundation

The deterministic workflow layer remains the source of truth:

- reservations
- policies
- workflow rules
- action logging

AI components assist with interpretation and retrieval but do not bypass business controls.

## Planned AI architecture

```
Guest message
      ↓
Conversation manager
      ↓
Intent/router agent
      ↓
Workflow controller
      ↓
Tools
 ├── reservation lookup
 ├── policy retrieval
 └── action services
      ↓
Response generation
      ↓
Trace + evaluation
```

## Design principles

- Separate reasoning from execution
- Use tools instead of hidden database access
- Keep workflows observable
- Store agent decisions
- Evaluate against business scenarios
- Keep humans involved for sensitive actions
