from typing import List
from datetime import date
from datetime import datetime
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from src.domain.uses_cases.crop_use_cases import CropUseCase
from src.domain.models.weeks_statistics_model import WeeksStatisticsModel


class WeeksStatisticsUseCase:
    @staticmethod
    async def get_future_weeks_harvesting(harvest_id: int, token: str) -> List[WeeksStatisticsModel]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_all_crops_harvest_by_id(harvest_id)
            weeks_model_list = [
                WeeksStatisticsModel(
                    initial_week=c.approximate_durability_date.isocalendar()[1],
                    final_week=c.approximate_durability_date.isocalendar()[1]+c.approximate_weeks_crop_durability
                )
                for c in crops
            ]
            return weeks_model_list
