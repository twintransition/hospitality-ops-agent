# Hospitality Operations Agent Execution Flow

## Runtime graph

```
START
 |
 v
Intent Agent
 |
 v
Knowledge Retrieval
 |
 v
Workflow Controller
 |
 v
Tool Execution
 |
 v
Response Agent
 |
 v
Audit + Evaluation
```

## Design rules

- The LLM interprets and communicates.
- Operational workflows enforce business rules.
- Tools provide controlled access to business capabilities.
- Responses are generated from verified state.
- Every execution should leave a trace.
