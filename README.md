# Simple Retrieval API

This repository contains a small example showing how to connect a frontend to a backend using HTTP.

Overview

- Backend: FastAPI application exposing `POST /api/search` that returns matching documents from an in-memory corpus.
- Frontend: `index.html` — a single static page that sends a JSON POST request via `fetch()` to the backend and renders results.

Files

- `backend.py` — FastAPI server implementing the `/api/search` endpoint.
- `index.html` — Static frontend UI that calls the API.
- `requirements.txt` — Minimal Python dependencies (`fastapi`, `uvicorn`).

Quick start

```bash
# 1. Clone this repo (if you haven't already)
git clone https://github.com/Srikanthk9k/API-connecting-application.git
cd API-connecting-application

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Start the backend server (runs on http://127.0.0.1:8000)
python backend.py

# 4. Serve the frontend (or open index.html directly)
# Option A - serve static files (recommended):
python -m http.server 8080
# then open http://127.0.0.1:8080/index.html

# Option B - open the file directly in your browser (file://...)
```

API

- POST `/api/search`
  - Request JSON: `{ "query": "<your search term>" }`
  - Response: JSON with keys: `status`, `query_received`, `match_count`, `data` (array of matching documents)

Notes and recommendations

- CORS is configured to allow all origins in this example for simplicity. Lock this down for production.
- The `MOCK_CORPUS` is an in-memory list used for demonstration. Replace with a real document store or vector DB for production use.
- Consider containerizing this service with Docker for easier deployment.

License

This example is provided as-is under the MIT license. Feel free to reuse and adapt.
