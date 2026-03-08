# Python FastAPI Sample Webpage

This is a simple sample project that uses FastAPI to serve an HTML/CSS webpage. It also includes a GitHub Actions workflow that runs a pipeline for testing.

## Features

- FastAPI app serving static HTML and CSS
- Basic test using pytest
- GitHub Actions pipeline for automated testing

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the environment:
   ```bash
   # Windows
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   uvicorn main:app --reload
   ```
5. Navigate to `http://127.0.0.1:8000` in your browser.

## Running Tests

```bash
pytest
```

## GitHub Actions

The workflow defined in `.github/workflows/ci.yml` installs dependencies and runs tests on push or pull request.