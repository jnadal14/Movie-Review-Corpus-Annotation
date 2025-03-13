"""
models.py

This file defines the Pydantic models used for data validation and serialization.
We define a Review model that represents a movie review, with an optional annotation label.
"""

from pydantic import BaseModel
from typing import Optional

class Review(BaseModel):
    review_id: str
    text: str
    annotation_label: Optional[str] = None
