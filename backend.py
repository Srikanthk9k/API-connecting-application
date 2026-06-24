import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize the application
app = FastAPI(title="Simple Retrieval API")

# Configure CORS so the frontend can call this API from a different origin
# In production, specify your frontend's actual domain
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:8080").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Specify your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the expected structure of the incoming request payload
class SearchQuery(BaseModel):
    query: str


# Mock data simulating a vector database or document store
MOCK_CORPUS = [
    {"id": 1, "title": "AWS Data Architecture", "content": "Patterns for highly scalable data pipelines."},
    {"id": 2, "title": "Agentic Workflows", "content": "Optimizing generative AI agent ecosystems."},
    {"id": 3, "title": "RAG Pipelines", "content": "Building robust retrieval-augmented generation systems in Python."}
]


@app.post("/api/search")
async def perform_search(request: SearchQuery):
    """
    Accepts a query string from the frontend and returns matching documents.
    """
    search_term = request.query.lower()

    # Simple list comprehension to simulate retrieval logic
    results = [
        doc for doc in MOCK_CORPUS
        if search_term in doc["title"].lower() or search_term in doc["content"].lower()
    ]

    return {
        "status": "success",
        "query_received": request.query,
        "match_count": len(results),
        "data": results,
    }


if __name__ == "__main__":
    # Allows starting the server with `python backend.py`
    import uvicorn

    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(app, host=host, port=port, reload=True)
