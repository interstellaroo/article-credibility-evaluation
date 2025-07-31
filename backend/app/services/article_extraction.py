from newspaper import Article
from bs4 import BeautifulSoup
from app.models import ArticleData

def extract_article(url: str):
    article = Article(url)
    article.download()
    article.parse()

    return ArticleData(
        title=article.title,
        text=article.text,
        paragraphs=extract_paragraphs(article.html),
        authors=article.authors,
        publish_date=article.publish_date
    )
    
def extract_paragraphs(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
    return paragraphs