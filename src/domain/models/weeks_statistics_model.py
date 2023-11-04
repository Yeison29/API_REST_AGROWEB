from pydantic import BaseModel


class WeeksStatisticsModel(BaseModel):
    initial_week: int
    final_week: int
