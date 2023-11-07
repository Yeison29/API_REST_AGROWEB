from pydantic import BaseModel
from typing import List
from src.domain.models.weeks_model import WeeksModel


class WeeksStatisticsModel(BaseModel):
    initial_week: int
    final_week: int
    weeks: List[WeeksModel]
