# CI/CD Task API

A simple task management API built with Python and FastAPI, with Docker support and automated CI/CD using GitHub Actions.

## Features

- `GET /health` — Check API health.
- `POST /tasks` — Create a new task.
- `GET /tasks` — List all tasks.
- Automated tests and Docker build on Pull Requests.
- Automated GitHub Releases and Docker image publishing to GHCR when a version tag is pushed.

## Run locally

### 1. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pytest httpx
```

### 2. Start the API

```bash
uvicorn main:app --reload
```

The API is available at `http://localhost:8000`.

Interactive API documentation: `http://localhost:8000/docs`.

### 3. Run tests

```bash
pytest
```

## Run with Docker

### Build the image

```bash
docker build -t ci-cd-task:local .
```

### Start the container

```bash
docker run --rm -p 8080:8000 ci-cd-task:local
```

Open `http://localhost:8080/health` to check the service.

## Pull a released image from GHCR

Replace `OWNER` with the GitHub username or organization that owns the repository, and `VERSION` with a published tag such as `v1.0.0`.

```bash
docker pull ghcr.io/OWNER/ci-cd-task:VERSION
docker run --rm -p 8080:8000 ghcr.io/OWNER/ci-cd-task:VERSION
```

For this repository, the image name is expected to be `ghcr.io/eugene-keen/ci-cd-task`.

## CI/CD workflow

- Pull Requests targeting `main` or `develop` run the tests and build the Docker image.
- Pushing a version tag such as `v1.0.0` triggers the release workflow.
- The release workflow runs tests before publishing the Docker image to GitHub Container Registry and creating a GitHub Release with a downloadable ZIP archive.

## Notes

Tasks are stored in memory, so they are reset when the API process restarts. This project is intended as a learning/demo application.
