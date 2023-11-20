from typing import List
from datetime import datetime, date, timedelta
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from src.domain.uses_cases.crop_use_cases import CropUseCase
from src.domain.uses_cases.user_use_cases import UserUseCase
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

        df_sorted["start_date"] = df_sorted.apply(lambda row: datetime.strptime(f"{int(row['initial_year'])} "
                                                                                f"{int(row['week'])} 1", "%G %V %u"),
                                                  axis=1)
        start_date = datetime.now() - timedelta(days=7)
        end_date = df_sorted["start_date"].max() + timedelta(days=7)
        date_range = pd.date_range(start_date, end_date, freq="W-Mon")
        all_weeks_df = pd.DataFrame(date_range, columns=["start_date"])
        all_weeks_df["week"] = all_weeks_df["start_date"].dt.strftime("%U").astype(int) + 1
        all_weeks_df["initial_year"] = all_weeks_df["start_date"].dt.year
        all_weeks_df["initial_month"] = all_weeks_df["start_date"].dt.month

        merged_df = pd.merge(all_weeks_df, df_sorted, how="left", on=["week", "initial_year", "initial_month"])

        merged_df["total_hectares"].fillna(0, inplace=True)
        merged_df = merged_df.drop(merged_df.loc[merged_df['week'] > 52].index)

        df_result = merged_df.drop(['start_date_x', 'start_date_y'], axis=1)

        dict_from_df = df_result.to_dict(orient='records')
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
        df_group = (df.groupby(['municipality_id', 'code_municipality', 'name_municipality', 'harvest_id',
                                'name_harvest', 'code_harvest'])['total_hectares'].sum().
                    reset_index())
        df_sorted = df_group.sort_values(by='total_hectares')
        dict_from_df = df_sorted.to_dict(orient='records')
        return dict_from_df

    @staticmethod
    async def most_widely_planted_crops(token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_most_widely_planted_crops()
            df = pd.DataFrame([model.__dict__ for model in crops])
            df_group = (df.groupby(['harvest_id',
                                    'name_harvest', 'code_harvest'])['hectares'].sum().
                        reset_index())
            df_sorted = df_group.sort_values(by='hectares')
            df_top_five = df_sorted.head(5)
            dict_from_df = df_top_five.to_dict(orient='records')
            return dict_from_df

    @staticmethod
    async def statistics_genres(token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            genders = await UserUseCase.statistics_genres()
            df = pd.DataFrame([model.__dict__ for model in genders])
            df_group = (df.groupby(['gender_id',
                                    'name_gender', 'code_gender'])['gender_id'].value_counts().reset_index())
            dict_from_df = df_group.to_dict(orient='records')
            return dict_from_df

    @staticmethod
    async def age_range(token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            ages = await UserUseCase.age_renge()
            df = pd.DataFrame([model.__dict__ for model in ages])
            df['birthdate_user'] = pd.to_datetime(df['birthdate_user'])
            df['age'] = df['birthdate_user'].apply(lambda x: (datetime.now() - x).days // 365)
            range_age = [0, 18, 30, 50, float('inf')]
            df['range_age'] = pd.cut(df['age'], bins=range_age, labels=['0-18', '19-30', '31-50', '51+'], right=False)
            count_age = df.groupby('range_age').size().reset_index(name='count')
            dict_from_df = count_age.to_dict(orient='records')
            return dict_from_df
