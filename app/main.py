from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

load_dotenv()
app = FastAPI()

app.mount("/static", StaticFiles(directory="../client/build/static", html=True), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return FileResponse('../client/build/index.html')


@app.get("/get-keyword/")
async def get_keyword(date: str):
    api_key = os.getenv("GUARDIAN_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not configured")
    
    url = f"https://content.guardianapis.com/search?from-date={date}&to-date={date}&api-key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError, if one occurred
        data = response.json()
        articles = data.get("response", {}).get("results", [])
        
        # Combine all article titles for keyword extraction
        all_titles = ' '.join([article['webTitle'] for article in articles])
        
        # Extract the most common noun from the titles
        keyword = extract_most_common_noun(all_titles)
        
        return {"keyword": keyword}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

# Healthcheck endpoint to make sure the server is running
@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

def extract_most_common_noun(text: str) -> str:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')
    
    # Tokenize the text
    words = word_tokenize(text)
    
    # Filter out non-alphanumeric words and stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    
    # Tag parts of speech and extract nouns
    nouns = [word for (word, pos) in nltk.pos_tag(words) if pos.startswith('NN')]
    
    # Find the most common noun
    most_common_nouns = Counter(nouns).most_common()
    keyword = most_common_nouns[0][0] if most_common_nouns else 'No keyword found'
    
    return keyword

@app.get("/{path:path}")
async def serve_file(path: str):
    file_path = "../client/build/" + path
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        raise HTTPException(status_code=404)
    return FileResponse(str(file_path))
