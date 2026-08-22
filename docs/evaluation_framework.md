# Agent Evaluation Framework

A production agent requires evaluation beyond whether a response sounds natural.

## Evaluation loop

```
Scenario
   ↓
Agent execution
   ↓
Observed actions
   ↓
Expected workflow
   ↓
Evaluation result
```

## Scenario components

Each scenario should define:

- guest request
- available context
- expected intent
- required tools
- acceptable actions
- final outcome

## Example

Late check-in:

Input:

"My flight arrives after midnight. Can I still check in?"

Expected:

- identify late check-in intent
- retrieve reservation
- retrieve late check-in policy
- create approved response
- log action

## Metrics

Future evaluation will track:

- workflow completion
- tool selection accuracy
- policy compliance
- response quality
- escalation correctness
