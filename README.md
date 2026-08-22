# Hospitality Ops Agent

An AI-powered hospitality operations agent that combines guest communication, SOP-guided reasoning, operational data, and workflow automation.

## Project Goal

Build a realistic AI operations assistant that can handle guest requests by:

- understanding guest intent
- retrieving relevant hotel SOPs
- checking operational data
- recommending or executing actions
- maintaining an audit trail

This project focuses on **workflow automation**, not a simple chatbot.

## MVP Workflow

Guest request → Intent understanding → SOP retrieval → Operational check → Decision → Response / Task creation

## Architecture

```
Frontend (Next.js)
        |
FastAPI Backend
        |
LangGraph Agent Workflow
        |
PostgreSQL + pgvector
        |
SOP Knowledge Base
```

## Planned Stack

- Python + FastAPI
- LangGraph agent orchestration
- PostgreSQL
- pgvector for RAG
- Next.js + TypeScript dashboard
- Docker deployment

## Current MVP

Guest Communication Agent:

Example:

> "I will arrive after midnight. Can I still check in?"

The agent will evaluate the request using reservation data, hotel policies, and workflow rules before generating a response.
