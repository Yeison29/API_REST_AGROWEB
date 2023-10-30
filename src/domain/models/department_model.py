from pydantic import BaseModel
from typing import Optional


class DepartmentModelIn(BaseModel):
    name_department: str
    code_department: str
    country_id: int


class DepartmentModelOut(DepartmentModelIn):
    id_department: int


class DepartmentModelUpdate(DepartmentModelIn):
    name_department: Optional[str] = None
    code_department: Optional[str] = None
