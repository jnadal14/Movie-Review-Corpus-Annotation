"""
routes.py

This file defines the API endpoints for our back-end. It contains two endpoints:
  - /search: Searches the corpus for reviews containing a query string.
  - /annotations: Retrieves all reviews with the specified annotation label. 
"""

from fastapi import APIRouter, Request, HTTPException
from typing import List
from search import search_reviews
from models import Review

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
    corpus = request.app.state.corpus
    if not corpus:
        raise HTTPException(status_code=500, detail="Corpus not loaded")
    results = search_reviews(q, annotated, corpus)
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
    corpus = request.app.state.corpus
    reviews = []
    for review in corpus:
        if review.annotation_label == annotation_label.lower():
            reviews.append(review)
    if not reviews:
        raise HTTPException(status_code=404, detail="Review not found")
    return reviews
