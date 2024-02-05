from pydantic import BaseModel
from typing import Optional


class MunicipalityModelIn(BaseModel):
    name_municipality: str
    department_id: int


class MunicipalityModelOut(MunicipalityModelIn):
    id_municipality: int


class MunicipalityModelUpdate(MunicipalityModelIn):
    name_municipality: Optional[str] = None
    code_municipality: Optional[str] = None
