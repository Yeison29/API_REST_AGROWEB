from pydantic import BaseModel
from typing import Optional


class GenderModelIn(BaseModel):
    name_gender: str
    code_gender: str


class GenderModelOut(GenderModelIn):
    id_gender: int


class GenderModelUpdate(GenderModelIn):
    name_gender: Optional[str] = None
    code_gender: Optional[str] = None
