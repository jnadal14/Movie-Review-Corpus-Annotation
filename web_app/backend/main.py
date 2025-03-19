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
from fastapi.staticfiles import StaticFiles
from .data_loader import create_index, get_index
from .routes import router

app = FastAPI(
    title="Movie Review Corpus API",
    description="API for searching and retrieving annotated movie reviews.",
    version="1.0.1",
)

# currently CORS allows requests from any origin (should adjust later?)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # should restrict to frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create the whoosh index at startup and load to app.state
@app.on_event("startup")
def startup_event():
    create_index() #build index from jsonl corpus
    app.state.index = get_index() #index store in app.state for endpoints

# include API routes (defined in routes.py)
app.include_router(router)

# run app when executing this file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# serve the frontend build as static files from root URL
app.mount("/", StaticFiles(directory="/app/web_app/backend/static", html=True), name="static")

