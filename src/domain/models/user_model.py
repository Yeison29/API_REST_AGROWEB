from pydantic import Field
from datetime import date
from pydantic import BaseModel
from typing import Optional


class UserModelIn(BaseModel):
    name_user: str
    lastname_user: str
    email_user: str
    phone_user: str
    id_document_user: str
    birthdate_user: date = Field(None, description="Fecha de nacimiento (YYYY-MM-DD)")
    gender_id: int


class UserModelOut(UserModelIn):
    id_user: int


class UserModelUpdate(UserModelIn):
    name_user: Optional[str] = None
    lastname_user: Optional[str] = None
    email_user: Optional[str] = None
    type_document_user: Optional[str] = None
    id_document_user: Optional[str] = None
    birthdate_user: Optional[date] = Field(None, description="Fecha de nacimiento (YYYY-MM-DD)")
