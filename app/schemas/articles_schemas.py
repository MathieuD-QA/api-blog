from pydantic import BaseModel


class CreatedArticle(BaseModel):
    title: str
    author: str
