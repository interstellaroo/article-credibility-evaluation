from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class URLInput(BaseModel):
    url: HttpUrl
    
class ArticleData(BaseModel):
    title: str
    text: str
    paragraphs: List[str]
    authors: List[str]
    publish_date: Optional[datetime]