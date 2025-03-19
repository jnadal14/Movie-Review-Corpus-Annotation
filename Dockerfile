# build React frontend
FROM node:16 as build-frontend
WORKDIR /app/web_app/frontend
# copy package files and install dependencies
COPY web_app/frontend/package*.json ./
RUN npm install
# copy the rest of the frontend source code and build the app
COPY web_app/frontend/ ./
RUN npm run build

# set up backend with corpus data
FROM python:3.11-slim
WORKDIR /app/web_app/backend

#system dependencies 
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# copy backend code into container
COPY web_app/backend/ ./
# copy corpus data
COPY data/ ./data/
# copy the built frontend (static files) into backend's static directory
# backend code should be set up to serve static files from "backend/static"
COPY --from=build-frontend /app/web_app/frontend/build/ ./static/

# install python dependencies
# (Make sure these are the dependencies needed by your backend)
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn whoosh pydantic

#port
EXPOSE 8000

# start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
