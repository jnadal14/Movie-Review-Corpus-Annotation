"""
data_loader.py

Loads the movie review corpus from a JSON Lines (JSONL) file and builds a Whoosh index for efficient search.
Each line in the JSONL file should be a JSON object with the following keys:
  - id: Unique identifier for the review.
  - text: A JSON-formatted string containing keys like "Reviewer", "Profile_URL", and "Review".
  - label: The annotation label (could be numeric, so we convert it to string).
This module extracts only the "Review" value from the text field and builds an index.
"""

import os
import json
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer

def create_index():
    """
    Creates a Whoosh index from the JSONL corpus if it doesn't already exist.
    The index is stored in the 'indexdir' folder.
    """
    # build the directory path where the index will be stored.
    index_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "annotated_dataset", "indexdir")
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
        #print("Created index directory:", index_dir)
    else:
        print("Index directory already exists:", index_dir)
        
    # define the schema for the index
    schema = Schema(
        review_id=ID(stored=True, unique=True), 
        text=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        annotation_label=TEXT(stored=True) 
    )
    

    if not index.exists_in(index_dir):
        idx = index.create_in(index_dir, schema)
        writer = idx.writer()
        # build the path to the JSONL corpus file.
        data_file = os.path.join(os.path.dirname(__file__), "..", "..", "data", "annotated_dataset", "annotated_database.jsonl")
        #print("Indexing file from:", data_file) #for debugging
        
        line_count = 0
        with open(data_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue 
                line_count += 1
                if line_count % 100 == 0:
                    print(f"Processed {line_count} lines")
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    print("Skipping malformed line")
                    continue
                    
                # convert review_id and annotation_label to string to make unicode -- this might be messing up the annotation filtering, not sure. 
                review_id = str(record.get("id", ""))
                
                # extract text field
                raw_text = record.get("text", "")
                
                try:
                    # parse the raw_text into dict.
                    text_obj = json.loads(raw_text)
                    # extract only the "Review" key -- i added this bc it looks better in the front-end. but we can keep reviewer too, for example.
                    review_text = text_obj.get("Review", "")
                except json.JSONDecodeError:
                    review_text = raw_text
                # convert annotation_label to string.
                annotation_label = str(record.get("label", ""))
                writer.add_document(review_id=review_id, text=review_text, annotation_label=annotation_label)
        writer.commit()
        print("Index creation complete. Total lines processed:", line_count) #for debugging
    else:
        print("Index already exists. Skipping index creation.") #for debugging

def get_index():
    """
    Opens and returns the Whoosh index.
    """
    index_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "annotated_dataset", "indexdir")
    return index.open_dir(index_dir)