from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serve the home page."""
    return templates.TemplateResponse(request, "index.html")

@app.get("/about", response_class=HTMLResponse)
def read_about(request: Request):
    """Serve the about page."""
    return templates.TemplateResponse(request, "about.html")
