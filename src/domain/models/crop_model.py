from pydantic import BaseModel
from typing import Optional
from pydantic import Field
from datetime import date


class CropModelIn(BaseModel):
    hectares: float
    seed_time: date = Field(None, description="Fecha de siembra (YYYY-MM-DD)")
    approximate_durability_date: date = Field(None, description="Fecha aproximada ha cosechar (YYYY-MM-DD)")
    approximate_weeks_crop_durability: int
    harvest_id: int
    user_id: int


class CropModelOut(CropModelIn):
    id_crop: int


class CropModelUpdate(CropModelIn):
    hectares: Optional[float] = None
    seed_time: Optional[date] = Field(None, description="Fecha de siembra (YYYY-MM-DD)")
    approximate_durability_date: Optional[date] = Field(None, description="Fecha aproximada ha cosechar (YYYY-MM-DD)")
    approximate_weeks_crop_durability: Optional[int] = None
    harvest_id: Optional[int] = None
    user_id: Optional[int] = None
