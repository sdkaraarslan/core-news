from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "headline": "Welcome to Core News"})
    
@app.get("/news/{date}")
async def get_news(date: str, request: Request):
    api_key = os.getenv("GUARDIAN_API_KEY")
    url = f"https://content.guardianapis.com/search?from-date={date}&to-date={date}&api-key={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("response", {}).get("results", [])
    return templates.TemplateResponse("index.html", {"request": request, "articles": articles, "headline": "Top News"})
