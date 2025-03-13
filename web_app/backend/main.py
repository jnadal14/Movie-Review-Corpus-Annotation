"""
main.py

Entry point for FastAPI back-end.
  - Creates the FastAPI app instance.
  - Sets up CORS middleware.
  - Loads the movie review corpus once on startup (for efficient querying).
  - Includes the API routes defined in routes.py.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_corpus
from routes import router

app = FastAPI(
    title="Movie Review Corpus API",
    description="API for searching and retrieving annotated movie reviews.",
    version="1.0.0",
)

# currently CORS allows requests from any origin (should adjust later?)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # should restrict to frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the corpus once at startup and store it in app state
@app.on_event("startup")
def startup_event():
    app.state.corpus = load_corpus() #should maybe include error handling here to ensure corpus is loading right?

# Include API routes (defined in routes.py)
app.include_router(router)

# Run app when executing this file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
