"""
search.py

This module contains the search functionality for the corpus.
It provides a function that searches for reviews based on a query string,
and can optionally filter out reviews without annotations.
"""

#first try, might need to use whoosh or something else depending on size

from typing import List
from models import Review

def search_reviews(query: str, annotated_only: bool, corpus: List[Review]) -> List[Review]: 
    """
    Search the corpus for reviews that contain the query string.

    Args:
      query (str): The search query.
      annotated_only (bool): If True, only return reviews with an annotation label.
      corpus (List[Review]): The preloaded list of reviews.

    Returns:
      List[Review]: Reviews matching the query criteria.
    """
    results = []
    query_lower = query.lower()
    for review in corpus:
        # skip un-annotated reviews if requested by user
        if annotated_only and (not review.annotation_label or review.annotation_label.strip() == ""):
            continue
        if query_lower in review.text.lower():
            results.append(review)
    return results
