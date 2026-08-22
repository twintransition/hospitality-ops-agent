# Running the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API health check:

```
GET /health
```

Workflow endpoint:

```
POST /workflows/late-checkin
```
