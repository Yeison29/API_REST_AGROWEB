from pydantic import BaseModel


class WeeksModel(BaseModel):
    week: int
    initial_month: int
    final_month: int
    initial_year: int
    final_year: int
    total_hectares: float
