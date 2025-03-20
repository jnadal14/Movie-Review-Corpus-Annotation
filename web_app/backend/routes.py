"""
routes.py

This file defines the API endpoints that query whoosh index. It contains two endpoints:
  - /search: Searches the corpus for reviews containing a query string.
  - /annotations: Retrieves all reviews with the specified annotation label. 
"""

from fastapi import APIRouter, Request, HTTPException
from typing import List
from .search import search_reviews_whoosh
from .models import Review

router = APIRouter()

@router.get("/search", response_model=List[Review])
async def search_endpoint(q: str, annotated: bool = False, request: Request = None): #annotated bool still needs to be added to front end!
    """
    GET /search

    Params:
      - q: The search query string.
      - annotated: Boolean flag; if True, only returns reviews that have an annotation.
    
    Returns:
      A list of Review objects that match the search criteria.
    """
    #retrieve index from app state
    index = request.app.state.index
    
    #if not index:
        #raise HTTPException(status_code=500, detail="Corpus not loaded")
    
    results = search_reviews_whoosh(index, q, annotated)
    return results

@router.get("/annotations", response_model=List[Review])
async def annotation_endpoint(annotation_label: str, request: Request = None): #endpoint still missing front end!
    """
    GET /annotations

    Params:
      - annotation_label: retrieve all reviews annotated with this label category.
    
    Returns:
      The reviews corresponding to the given annotation label.
    """
    index = request.app.state.index

    from whoosh.qparser import QueryParser #build query for annotation_label
    
    with index.searcher() as searcher:
        parser = QueryParser("annotation_label", index.schema)
        #enclose in quotes for exact match
        query = parser.parse(f'"{annotation_label}"')
        results = searcher.search(query, limit=None)
        if results:
            reviews = [
                Review(
                    review_id=doc["review_id"],
                    text=doc["text"],
                    annotation_label=doc.get("annotation_label", "")
                )
                for doc in results
            ]
            return reviews
        else:
            raise HTTPException(status_code=404, detail="Review not found")

#this one is just to check that 1001 docs were retrieved --delete later
@router.get("/health") 
async def health_endpoint(request: Request):
    index = request.app.state.index
    with index.searcher() as searcher:
        count = searcher.doc_count()
        sample = searcher.stored_fields(0) if count > 0 else {}
    return {"status": "ok", "document_count": count, "sample_document": sample}

