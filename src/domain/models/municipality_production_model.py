from pydantic import BaseModel
from typing import Optional


class MunicipalityProductionModelOut(BaseModel):
    name_municipality: str
    municipality_id: int
    code_municipality: str
    harvest_id: int
    code_harvest: str
    name_harvest: str
    total_hectares: float
