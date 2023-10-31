from pydantic import BaseModel
from typing import Optional


class HarvestModelIn(BaseModel):
    name_harvest: str
    code_harvest: str


class HarvestModelOut(HarvestModelIn):
    id_harvest: int


class HarvestModelUpdate(HarvestModelIn):
    name_harvest: Optional[str] = None
    code_harvest: Optional[str] = None
