# Backend MVP

FastAPI service for the hospitality operations agent.

Current implementation stage:

- operational data models
- workflow execution skeleton
- tool interfaces
- agent action logging

The backend is intentionally workflow-first. LLM integration will be added after deterministic business workflows are validated.

Planned modules:

```
backend/
├── app/
│   ├── api/
│   ├── agents/
│   ├── workflows/
│   ├── retrieval/
│   ├── database/
│   └── services/
└── tests/
```

Responsibilities:

- expose operational APIs
- execute agent workflows
- connect database tools
- manage SOP retrieval
- store agent actions
