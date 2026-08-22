# Agent Tool Interface Design

Agents should interact with hospitality systems through explicit tools.

## Tool principle

The model should not directly manipulate operational data.

Instead:

```
Agent
 ↓
Tool interface
 ↓
Business service
 ↓
Database
```

## Initial tools

### Reservation lookup

Purpose:

Retrieve reservation context required for decisions.

Example:

```
find_reservation(reservation_id)
```

Returns:

- guest information
- booking status
- dates
- room information

### Policy retrieval

Purpose:

Retrieve applicable SOP/policy information.

Example:

```
get_policy(policy_type)
```

### Action execution

Purpose:

Perform approved operational updates.

Examples:

- update arrival note
- create operational task
- send guest communication

## Future MCP direction

Tool interfaces should remain independent from the model provider so they can later be exposed through standard tool protocols.
