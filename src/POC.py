import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configuration
movie_slug = "oppenheimer-2023"  
base_url = f"https://letterboxd.com/film/{movie_slug}/reviews/by/activity/page/"

# Mimic a request from a real web browser.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

reviews_data = []
page = 1
max_reviews = 100  

while len(reviews_data) < max_reviews:
    url = f"{base_url}{page}/"
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

    for review in reviews:
        if len(reviews_data) >= max_reviews:
            break

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

            # Append data
            reviews_data.append({
                "Reviewer": reviewer,
                "Profile_URL": profile_url,
                "Movie": movie_slug.title(),
                "Review": review_text
            })

        # Skip if there's an issue with extracting data
        except AttributeError:
            continue  

    time.sleep(2)
    
    page += 1


# Saving the corpus data
with open("data/POC_data.txt", "w", encoding="utf-8") as file:
    for review in reviews_data:
        file.write(f"Movie: {review['Movie']}\n")
        file.write(f"Reviewer: {review['Reviewer']}\n")
        file.write(f"Profile URL: {review['Profile_URL']}\n")
        file.write(f"Review:\n")
        file.write(f"{review['Review']}\n")
        file.write("-" * 80 + "\n")

print(f"Saved {len(reviews_data)} reviews to 'POC_data.txt'")
