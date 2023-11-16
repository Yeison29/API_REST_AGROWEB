from typing import List
from datetime import datetime, date, timedelta
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from src.domain.uses_cases.crop_use_cases import CropUseCase
from src.domain.models.weeks_statistics_model import WeeksStatisticsModel
from src.domain.models.weeks_model import WeeksModel
from src.domain.models.municipality_production_model import MunicipalityProductionModelOut
import pandas as pd
import pytz

time_zone = pytz.timezone('America/Bogota')


class WeeksStatisticsUseCase:
    @staticmethod
    async def get_future_weeks_harvesting(harvest_id: int, token: str) -> List[dict]:
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
            response = await WeeksStatisticsUseCase.purge_data_weeks(weeks_model_list)
            return response

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

    @staticmethod
    async def purge_data_weeks(data: List[WeeksStatisticsModel]) -> List[dict]:
        weeks_list = [week for item in data for week in item.weeks]
        df = pd.DataFrame([model.__dict__ for model in weeks_list])
        df_group = df.groupby(['week', 'initial_year', 'initial_month'])['total_hectares'].sum().reset_index()
        df_sorted = df_group.sort_values(by='initial_year')
        #pd.set_option('display.max_columns', None)
        #pd.set_option('display.expand_frame_repr', False)
        dict_from_df = df_sorted.to_dict(orient='records')
        return dict_from_df

    @staticmethod
    async def get_most_planted_crop_by_municipality(token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_most_planted_crop_by_municipality()
            response = await WeeksStatisticsUseCase.purge_data_municipality_production(crops)
            return response

    @staticmethod
    async def purge_data_municipality_production(data: List[MunicipalityProductionModelOut]) -> List[dict]:
        df = pd.DataFrame([model.__dict__ for model in data])
        df_group = (df.groupby(['municipality_id', 'code_municipality', 'name_municipality'])['total_hectares'].sum().
                    reset_index())
        df_sorted = df_group.sort_values(by='total_hectares')
        dict_from_df = df_sorted.to_dict(orient='records')
        return dict_from_df
