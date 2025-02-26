# COLX_523_Group-Repository_David-Daoming-Jacob-Nicole

This repository contains the source code for our project, which focuses on scraping and analyzing human-written text from various online sources.

## **Project Overview**
The `src/` folder contains all project-related scripts and files. 

### **Current Implementation**
- `POC.py` is a proof-of-concept script designed to scrape movie reviews for *Oppenheimer (2023)* from [Letterboxd](https://letterboxd.com).
- `data_retrieval.py` is the working script to scrape 1,000 short reviews (under 60 words) or *Oppenheimer (2023)* from [Letterboxd](https://letterboxd.com).
- The script extracts and saves the following details to a file:
  - **Reviewer Username**
  - **Reviewer Profile URL**
  - **Review Content**
- The POC output is stored in `data/POC_data.txt`. The complete data output is stored under the `data/retrieved_docs` folder

## **Future Plans**
The `POC.py` is a simple implementation of web scraping to demonstrate our proof of concept. In the future, we plan to expand this project by using web scraping scripts and APIs to collect and analyze two categories of human-written text:
- Movie and book reviews
- News articles



## **Getting Started**
### **Prerequisites**
Ensure you have Python installed (preferably version 3.x) and install the required dependencies:
```sh
pip install requests beautifulsoup4 pandas
```
Change the path 'data_dir' to the path where you want the data to be stored.

