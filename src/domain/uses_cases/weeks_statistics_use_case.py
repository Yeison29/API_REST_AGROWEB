from typing import List
from datetime import datetime, date, timedelta
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from src.domain.uses_cases.crop_use_cases import CropUseCase
from src.domain.models.weeks_statistics_model import WeeksStatisticsModel
from src.domain.models.weeks_model import WeeksModel
import pytz

time_zone = pytz.timezone('America/Bogota')


class WeeksStatisticsUseCase:
    @staticmethod
    async def get_future_weeks_harvesting(harvest_id: int, token: str) -> List[WeeksStatisticsModel]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_all_crops_harvest_by_id(harvest_id)
            weeks_model_list = [
                WeeksStatisticsModel(
                    initial_week=await WeeksStatisticsUseCase.get_number_week(
                        c.approximate_durability_date.isocalendar()[1]),
                    final_week=await WeeksStatisticsUseCase.get_number_week(
                        c.approximate_durability_date.isocalendar()[1] + c.approximate_weeks_crop_durability - 1),
                    weeks=await WeeksStatisticsUseCase.get_weeks(
                        c.approximate_durability_date.isocalendar()[1],
                        c.approximate_durability_date.isocalendar()[1] + c.approximate_weeks_crop_durability - 1,
                        c.hectares,
                        c.approximate_durability_date
                    )
                )
                for c in crops
            ]
            return weeks_model_list

    @staticmethod
    async def get_weeks(initial_week: int, final_week: int, hectares: float, date_crop: date) -> List[WeeksModel]:
        week_now = datetime.now(time_zone).isocalendar()[1]
        print(week_now)
        if week_now > initial_week:
            initial_week += (week_now-initial_week)
        weeks_list = [
            WeeksModel(
                week=await WeeksStatisticsUseCase.get_number_week(i),
                initial_month=await WeeksStatisticsUseCase.get_initial_month_of_the_week(date_crop.year, i),
                final_month=await WeeksStatisticsUseCase.get_final_month_of_the_week(date_crop.year, i),
                initial_year=await WeeksStatisticsUseCase.get_initial_year_of_the_week(date_crop.year, i),
                final_year=await WeeksStatisticsUseCase.get_final_year_of_the_week(date_crop.year, i),
                total_hectares=hectares
            )
            for i in range(initial_week, final_week + 1)
        ]
        return weeks_list

    @staticmethod
    async def get_number_week(i: int) -> int:
        if i > 52:
            i -= 52
        return i

    @staticmethod
    async def get_initial_year_of_the_week(year: int, week: int) -> int:
        if week > 53:
            year += 1
            week -= 52
        initial_date = datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w')
        print(initial_date)
        return initial_date.year

    @staticmethod
    async def get_final_year_of_the_week(year: int, week: int) -> int:
        if week > 53:
            year += 1
            week -= 52
        date_crop = datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w')
        final_date = date_crop + timedelta(days=6)
        print(final_date)
        print("********")
        return final_date.year

    @staticmethod
    async def get_initial_month_of_the_week(year: int, week: int) -> int:
        if week > 53:
            year += 1
            week -= 52
        initial_date = datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w')
        return initial_date.month

    @staticmethod
    async def get_final_month_of_the_week(year: int, week: int) -> int:
        if week > 53:
            year += 1
            week -= 52
        date_crop = datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w')
        final_date = date_crop + timedelta(days=6)
        return final_date.month
