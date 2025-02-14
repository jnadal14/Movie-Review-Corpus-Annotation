# COLX_523_Group-Repository_David-Daoming-Jacob-Nicole

This repository contains the source code for our project, which focuses on scraping and analyzing human-written text from various online sources.

## **Project Overview**
The `src/` folder contains all project-related scripts and files. 

### **Current Implementation**
- `POC.py` is a proof-of-concept script designed to scrape movie reviews for *Oppenheimer (2023)* from [Letterboxd](https://letterboxd.com).
- The script extracts and saves the following details to a file:
  - **Movie Name**
  - **Reviewer Username**
  - **Reviewer Profile URL**
  - **Review Content**
- The output is stored in `data/POC_data.txt`.

## **Future Plans**
We plan to extend this project by scraping and analyzing a broader range of human-written text, including but not limited to:
- Movie and book reviews
- Social media posts
- News articles
- Forum discussions


## **Getting Started**
### **Prerequisites**
Ensure you have Python installed (preferably version 3.x) and install the required dependencies:
```sh
pip install requests beautifulsoup4 pandas

