# from viajei_api.schemas.user import User
from pydantic import BaseModel, ConfigDict

# class Story:
# name: str
# title: str
# email: str
# body: str


class StorySchemas(BaseModel):
    author: str
    title: str
    story: str


class StoryDB(StorySchemas):
    id: int


class StoryPublic(BaseModel):
    id: int
    title: str
    email: str
    model_config = ConfigDict(from_attributes=True)
