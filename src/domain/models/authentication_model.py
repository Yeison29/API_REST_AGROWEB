from pydantic import BaseModel
from typing import Optional


class AuthenticationModel(BaseModel):
    auth_password: str


class AuthenticationModelIn(AuthenticationModel):
    auth_email_user: str
    auth_user_id: int
    auth_disabled: bool


class AuthenticationModelOut(AuthenticationModelIn):
    id_auth: int


class AuthenticationModelUpdate(AuthenticationModelIn):
    auth_email: Optional[str] = None
    auth_password: Optional[str] = None
    auth_disabled: Optional[bool] = None
    auth_user_id: int

