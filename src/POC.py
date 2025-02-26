import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import json

# Configuration
webpage_url = f"https://letterboxd.com/film/oppenheimer-2023/reviews/by/activity/page/"
data_dir = "/Users/daomingliu/Desktop/mds-cl/523/COLX_523_Group-Repository_David-Daoming-Jacob-Nicole/data/retrieved_docs/"
last_doc_info_path = os.path.join(data_dir, f"last_doc_info.json")

# Mimic a request from a real web browser.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Page number
if os.path.exists(last_doc_info_path):
    with open(last_doc_info_path, "r") as f:
        doc_info = json.load(f)  # Load JSON data
        page = doc_info.get("last_page", -1)  # Page number from last time
        last_review_position_on_page = doc_info.get("review_position_on_page", -1) # The position of the last fetched review on the page 
        file_num = doc_info.get("last_doc", -1)  # The file number
else:
    page = 1
    last_review_position_on_page = 1
    file_num = 0 

    
# Max number of reviews to retrieve
max_reviews = 1000 

# Number of file (or review) retrieved

# Ensure the data directory exists, create one if not
os.makedirs(data_dir, exist_ok=True)



# Loop until reaches the maximum number of reviews
while file_num <= max_reviews:
    url = f"{webpage_url}{page}/"
    print(f"Fetching page {page}: {url}")

    # Load page content
    response = requests.get(url, headers=headers)
    
    # checks whether the HTTP request was successful.
    if response.status_code != 200:
        print("No more pages or blocked by website. Stopping.")
        break
    
    # Locate the reviews from the page content
    soup = BeautifulSoup(response.text, "html.parser")
    reviews = soup.find_all("li", class_="film-detail")
    
    # If no reviews found, stop the loop
    if not reviews:
        print("No more reviews found. Stopping.")
        break

    current_position_on_page = 0
    for review in reviews:
        # Loop until reaches the maximum number of reviews
        if file_num > max_reviews:
            print("Reached maximum documents")
            break

        current_position_on_page += 1
        # If the current review on this page is already fetched from last time, continue
        if current_position_on_page <= last_review_position_on_page:
            continue

        
        try:
            # Extract reviewer username
            reviewer_tag = review.find("strong", class_="name")
            reviewer = reviewer_tag.get_text(strip=True) if reviewer_tag else "Unknown"

            # Extract reviewer's profile URL
            profile_tag = review.find("a", class_="avatar")
            profile_url = "https://letterboxd.com" + profile_tag["href"] if profile_tag else "No URL"

            # Extract review text
            review_text_tag = review.find("div", class_="body-text")
            review_text = review_text_tag.get_text(strip=True) if review_text_tag else "No review text"

            # Cap the word count for each comment to 60 words
            if len(review_text.split(" ")) > 60:
                continue

            file_num += 1
            file_path = os.path.join(data_dir, f"review_doc_{file_num}.txt")
            
            reviews_data = {
                "Reviewer": reviewer,
                "Profile_URL": profile_url,
                "Review": review_text
            }

            # Save the review as a document
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(reviews_data, f)
                print(f"saved new document review_doc_{file_num}.txt")

            # Storing the current review-fetching progress
            doc_info = {
                "last_page": page,
                "review_position_on_page": current_position_on_page,
                "last_doc": file_num
            }
            with open(last_doc_info_path, "w") as f:
                json.dump(doc_info, f)

            
        # Skip if there's an issue with extracting data
        except AttributeError:
            continue  

    time.sleep(2)

    page += 1
    last_review_position_on_page = 0
    