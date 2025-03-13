"""
data_loader.py

This module contains functions to load the movie review corpus from a JSON file.
The expected format is a JSON array where each element is a review with:
  - review_id: string
  - text: string
  - annotation_label: string (optional)
If the file is not found, a small sample corpus is returned.
"""

import json
import os
from typing import List
from models import Review

def load_corpus() -> List[Review]:
    """
    Loads the corpus from data/corpus.json. If the file does not exist,
    returns a fallback sample corpus.

    Returns:
      List[Review]: List of Review objects loaded from the file or sample data.
    """

    data_file = os.path.join(os.path.dirname(__file__), "..", "..", "data", "annotated_dataset", "annotated_database.jsonl")
    
    corpus = []
    
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            # Read file line by line (since it's a JSONL file)
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                # Parse the line into a Python dictionary
                record = json.loads(line)
                # Extract the review ID
                review_id = record.get("id", "")
                # Extract and process the text field: it is a JSON-formatted string.
                raw_text = record.get("text", "")
                try:
                    # Convert the raw_text string into a dictionary
                    text_obj = json.loads(raw_text)
                    # Extract only the "Review" field from the text object.
                    review_text = text_obj.get("Review", "")
                except json.JSONDecodeError:
                    # If raw_text is not valid JSON, fall back to using it as-is.
                    review_text = raw_text
                # Extract the annotation label
                annotation_label = record.get("label", "")
                # Create a Review object using the extracted values.
                corpus.append(Review(review_id=review_id, text=review_text, annotation_label=annotation_label))
        return corpus
        
    except FileNotFoundError:
        # Sample corpus data if corpus.json is missing
        sample_data = [
            {
                "review_id": "001",
                "text": "This film was breathtaking and full of stunning visuals.",
                "annotation_label": "logos"
            },
            {
                "review_id": "002",
                "text": "I found the plot uninteresting and the characters shallow.",
                "annotation_label": "pathos"
            },
            {
                "review_id": "003",
                "text": "An average movie with some moments of brilliance.",
                "annotation_label": ""
            }
        ]
        corpus = [Review(**item) for item in sample_data]
        return corpus
