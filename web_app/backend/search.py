"""
search.py

This module contains the search functionality that queries Whoosh index for reviews matching criteria.
and can optionally filter out reviews without annotations.
"""

from typing import List
from models import Review
from whoosh.qparser import MultifieldParser

def search_reviews_whoosh(index, query: str, annotated_only: bool) -> List[Review]: 
    """
    Search the whoosh index for reviews that contain the query string.

    Args:
      index: the whoosh index object
      query (str): The search query.
      annotated_only (bool): If True, only return reviews with an annotation label.

    Returns:
      List[Review]: Reviews matching the query criteria.
    """
    with index.searcher() as searcher:
        #search in the text field
        parser = MultifieldParser(["text"], schema=index.schema)
        user_query = parser.parse(query)

        #execute query with no limit on results
        results = searcher.search(user_query, limit=None)

        #to filter non-annotated
        if annotated_only:
            results = [doc for doc in results if doc.get("annotation_label", "").strip() != ""] #this is not working, needs fixing

        #convert to Review object
        reviews = [
            Review(
                review_id=doc["review_id"], 
                text=doc["text"], 
                annotation_label=doc.get("annotation_label", "")
            )
            for doc in results
        ]
        return reviews
