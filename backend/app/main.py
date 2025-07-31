from fastapi import FastAPI, HTTPException
from .models import URLInput
from .services.article_extraction import extract_article

app = FastAPI(
    title="Credibility Evaluation",
    description="API for thesis project - Article Credibility Evaluation",
    version="v1.0",
)

@app.post("/api/process/url")
def process_url(data: URLInput):
    try:
        print(data.url)
        return extract_article(str(data.url))
    except Exception as e:
        print(f"URL Error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"There was an error during URL processing. Please try again...")