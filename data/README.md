# Hospitality Operations Agent Data

This project uses a workflow-oriented data design.

## Data layers

### Synthetic operational environment

A simplified hotel operations database used for development and evaluation:

- guests
- reservations
- rooms
- policies
- conversations
- agent actions

### External conversation data

Hospitality conversation datasets are referenced as evaluation material. External datasets are not copied into the repository unless licensing permits.

### Workflow scenarios

Scenario files define:

- guest request
- required tools/actions
- expected workflow outcome
- evaluation criteria

The goal is not chatbot response generation. The goal is testing whether an AI agent can follow hospitality operational procedures.
