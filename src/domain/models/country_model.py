from pydantic import BaseModel
from typing import Optional


class CountryModelIn(BaseModel):
    name_country: str
    code_country: str


class CountryModelOut(CountryModelIn):
    id_country: int


class CountryModelUpdate(CountryModelIn):
    name_country: Optional[str] = None
    code_country: Optional[str] = None
