from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize the application
app = FastAPI(title="Simple Retrieval API")

# Configure CORS so the frontend can call this API from a different origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set this to your frontend's origin
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

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
