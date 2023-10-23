from pydantic import BaseModel


class AuthorizeModel(BaseModel):
    username: str
    password: str
