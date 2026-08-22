# Hospitality Knowledge Retrieval Architecture

Current pipeline:

SOP documents

```
Markdown SOP
   |
   v
Chunking
   |
   v
Knowledge objects
   |
   v
Embedding provider
   |
   v
Vector backend
   |
   v
Knowledge Agent
   |
   v
Workflow decision
```

The vector backend is intentionally abstract. Production deployment will use
PostgreSQL with pgvector while keeping the agent interface unchanged.
