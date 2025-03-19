# COLX 523 - Advanced Corpus Linguistics

## Group Repository: David, Daoming, Jacob, Nicole

### **Project Overview**
This repository is dedicated to our group project for COLX 523 - Advanced Corpus Linguistics. The project involves building a corpus with annotation and a web interface, leveraging internet text sources to collect a sizable corpus (~1 million words).

### **Repository Structure**
```plaintext
COLX_523_Group-Repository_David-Daoming-Jacob-Nicole/
├── data/                # Raw and processed data files
├── documentation/       # Project-related documentation, meeting notes, and reports
├── src/                 # Source code for data collection, processing, and annotation
├── web_app/             # Contains the code for the interactive interface:
│     ├── frontend/      # The React application code for the user interface.
│     └── backend/       # The FastAPI application code for serving the API and static files  
├── .gitignore           # Files and directories to be ignored by Git
├── .dockerignore/       # Files and directories to be ignored by docker
├── instructions_movie-reviews.md   # Instructions for building and running the Docker image
├── Dockerfile/          # Dockerfile used to build a Docker image containing the entire project 
└── README.md            # Repository overview and guidelines
```

### To create and run Docker image:
Please refer to intructions_movie-reviews.md in root repo.

### Important File Locations (updated for sprint 3)
**Annotation Data**
- **Human Annotations**: Stored in **Excel files** under:
src/analysis/modified_corpus_batches/xlsx/
- **GPT annotations**: Stored in **json files** under:
src/analysis/modified_corpus_batches/json
- **Code for annotation & evaluation**: 
src/analysis/gpt and src/analysis/helper_methods

**Interannotator agreement study and Plan for the interface**: 
Both updated under documentation
