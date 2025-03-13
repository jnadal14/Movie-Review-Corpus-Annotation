# Backend API for Movie Review Corpus

## Overview
This FastAPI back-end provides API endpoints for searching and retrieving annotated movie reviews. It is designed to be modular, efficient, and easy to maintain.

### Key Features
- **Search Functionality:**  
  The `/search` endpoint accepts a query string (and an optional `annotated` flag) to return matching movie reviews. The search is performed in memory for fast response times.

- **Annotation Retrieval:**  
  The `/annotations` endpoint retrieves a specific review (including its annotation) based on a given `review_id`.

- **Efficiency:**  
  The corpus is loaded once at server startup, avoiding repeated disk I/O during each query.

- **Modular Design:**  
  Code is split into several modules:
  - `main.py`: App setup and startup logic.
  - `routes.py`: API endpoint definitions.
  - `search.py`: Contains the search logic.
  - `models.py`: Defines data models using Pydantic.
  - `data_loader.py`: Handles corpus loading from a JSON file.

## File Structure

backend/
├── main.py              # Entry point; creates the FastAPI app and loads the corpus.
├── routes.py            # API route definitions (endpoints).
├── search.py            # Functions that implement the search logic.
├── models.py            # Pydantic models for request/response validation.
└── data_loader.py       # Code to load the corpus from a JSON file.


## Running the Backend
1. **Install Dependencies:**  
   Make sure you have Python 3.8+ installed and run:
   ```bash
   pip install fastapi uvicorn pydantic```

2. From the backend directory run:
    ```bash
    uvicorn main:app --reload```
this starts the server on http://localhost:8000

3. Test the API:
   - Open http://localhost:8000/docs in browser to see interactive API documentation
   - Search endpoint example http://localhost:8000/search?q=film&annotated=true
   - Annotations Endpoint example: http://localhost:8000/annotations?review_id=001

## Integration with Frontend
In another terminal, run your front-end server using npm start.

Ensure your front-end (e.g., the React app already implemented) sends HTTP GET requests to:
- Search: http://localhost:8000/search
- Annotations: http://localhost:8000/annotations

