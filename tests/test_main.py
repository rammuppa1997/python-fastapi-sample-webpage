import sys
import os

# ensure project root is on sys.path for CI environments where tests run in a subdirectory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# note: templates directory requires jinja2 installed

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Infosys" in response.text

def test_read_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert "About This Project" in response.text
