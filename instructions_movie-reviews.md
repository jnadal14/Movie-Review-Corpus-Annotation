# Dockerization Instructions for Movie Review Corpus

This document explains step-by-step how to build and run the Docker image for our corpus interface project. These instructions should be helpful even if you have no previous Docker experience.

---
## Option 1: Download image from Drive (No image building required)

1. **Download the Tar file from Google Drive**
    Download `movie-reviews.tar` file from https://drive.google.com/drive/folders/1GVG8fABO9DKdAuBz1cJZpFvXxImRNHuV?usp=sharing
2. **Load image into Docker**
    Open a Terminal or Command Prompt and run:
   ```bash
   docker load -i movie-reviews.tar

   Make sure your path to movie-reviews.tar works.
3. **Run the container**
   Once the image is loaded, run with:
   ```bash
   docker run -p 8000:8000 movie-reviews

To see how to explore the interface, scroll down in this file to "What you should try".

If you run into any issues, scroll down to "Troubleshooting Tips".

## Option 2: Build your own image locally.

### Prerequisites

Before you begin, please ensure you have the following installed on your computer:

- **Docker:**  
  Download and install Docker from [docker.com](https://www.docker.com/get-started).  
  Make sure Docker is open and running before you continue!

- **Git (Optional):**  
  You should have cloned the project repository onto your machine.

---

### Building the Docker Image (Note: image takes some time to build. ~12 minutes on first build)

1. **Open a Terminal or Command Prompt.**

2. **Navigate to the Repository Root Directory:**  
   Change to the directory where you cloned the project. For example, if you cloned it to `~/projects/COLX_523_Group-Repository_David-Daoming-Jacob-Nicole`, run:
   ```bash
   cd ~/projects/COLX_523_Group-Repository_David-Daoming-Jacob-Nicole

3. Run the following command (from the root of the repo) to build the image.
    ```bash
    docker build -t movie-reviews .
    
(Note: remember the "." at the end of the command above!)
When the build completes, you should see a message confirming the image was built.

### Running the Docker container

1. After the image is built, run the following command to start the container and map the container's port 8000 to your local machine:
    ```bash
    docker run -p 8000:8000 movie-reviews

2. Access the interface: open your browser and go to
http://localhost:8000/


## What you should try:
When testing the interface, please follow these steps:

1. Homepage Navigation:

Verify that the homepage loads correctly.
Check that navigation options (e.g., "Search Reviews", "View Annotations") are visible.

2. Search Functionality:

Use the search input to enter keywords (e.g., "nolan" or "hello"). You may un-check "Show only annotated documents" to view both un-annotated and annotated reviews (by default, you will see only annotated documents).

Confirm that the search returns matching reviews.

You may scroll to the bottom to find "Return to Homepage".

3. Annotation Filtering:

On the "View Annotations" page, select one of the annotation categories ("Pathos", "Logos", or "Ethos").
Verify that only reviews with the chosen annotation are displayed.

You may scroll to the bottom to find "Return to Homepage".

4. API Documentation:

Visit http://localhost:8000/docs to access the interactive API documentation.
Ensure that you can view all the available endpoints and try them out.

5. Health Check (optional. not included in frontend):

Visit http://localhost:8000/health to see the number of documents indexed if you are interested. You will see number of documents after "document_count".

6. To stop running, simply press CTRL + C on the terminal.

## Troubleshooting tips

### Interface Does Not Load:

- Check the terminal for any error messages.
- Ensure Docker is running and that no other application is using port 8000.
- If necessary, run the container with a different local port (e.g., use -p 8080:8000 and then visit http://localhost:8080/).


### Port Conflicts:

If port 8000 is already in use, you can change the mapping by using a different local port:
    ```bash
    docker run -p 8080:8000 your_team_image

Then access the interface at http://localhost:8080/.


## Thank you!
Our Docker image packages the backend, frontend, and corpus data into a single container for easy distribution and review. Please follow these instructions carefully. If you have any questions or encounter any issues, feel free to ask for help.

Thank you for reviewing our project!
