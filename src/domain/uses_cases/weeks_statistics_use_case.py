from typing import List
from datetime import datetime, date, timedelta
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from src.domain.uses_cases.crop_use_cases import CropUseCase
from src.domain.uses_cases.user_use_cases import UserUseCase
from src.domain.uses_cases.haverst_use_cases import HarvestUseCase
from src.domain.uses_cases.municipality_use_cases import MunicipalityUseCase
from src.domain.models.weeks_statistics_model import WeeksStatisticsModel
from src.domain.models.weeks_model import WeeksModel
from src.domain.models.municipality_production_model import MunicipalityProductionModelOut
import pandas as pd
import pytz

time_zone = pytz.timezone('America/Bogota')


class WeeksStatisticsUseCase:
    @staticmethod
    async def get_future_weeks_harvesting(harvest_id: int, user_id: int, token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_all_crops_harvest_by_id(harvest_id, user_id)
            weeks_model_list = [
                WeeksStatisticsModel(
                    initial_week=await WeeksStatisticsUseCase.get_number_week(
                        c.approximate_durability_date.isocalendar()[1]),
                    final_week=await WeeksStatisticsUseCase.get_number_week(
                        c.approximate_durability_date.isocalendar()[1] + c.approximate_weeks_crop_durability - 1),
                    weeks=await WeeksStatisticsUseCase.get_weeks(
                        c.seed_time,
                        c.approximate_durability_date.isocalendar()[1],
                        c.approximate_durability_date.isocalendar()[1] + c.approximate_weeks_crop_durability - 1,
                        c.hectares,
                        c.approximate_durability_date
                    )
                )
                for c in crops
            ]
            print(weeks_model_list)
            response = await WeeksStatisticsUseCase.purge_data_weeks(weeks_model_list)
            return response

    @staticmethod
    async def get_weeks(initial_date: date, initial_week: int, final_week: int, hectares: float,
                        date_crop: date) -> List[WeeksModel]:
        print(date_crop)
        date_year_now = datetime.now(time_zone).year
        date_moth_now = datetime.now(time_zone).month
        date_day_now = datetime.now(time_zone).day
        if date_year_now < date_crop.year and date_moth_now < date_crop.month and date_day_now < date_crop.day:
            week_now = datetime.now(time_zone).isocalendar()[1]
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
        return initial_date.year

    @staticmethod
    async def get_final_year_of_the_week(year: int, week: int) -> int:
        if week > 53:
            year += 1
            week -= 52
        date_crop = datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w')
        final_date = date_crop + timedelta(days=6)
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
        if len(data) == 0:
            return []

        weeks_list = [week for item in data for week in item.weeks]
        df = pd.DataFrame([model.__dict__ for model in weeks_list])
        print(df)
        df_group = df.groupby(['week', 'initial_year'])['total_hectares'].sum().reset_index()
        df_sorted = df_group.sort_values(by='initial_year')

        df_sorted["start_date"] = df_sorted.apply(lambda row: datetime.strptime(f"{int(row['initial_year'])} "
                                                                                f"{int(row['week'])} 7", "%G %V %u"),
                                                  axis=1)
        start_date = datetime.now()
        end_date = df_sorted["start_date"].max() + timedelta(days=7)
        date_range = pd.date_range(start_date, end_date, freq="W-Mon")
        all_weeks_df = pd.DataFrame(date_range, columns=["start_date"])
        all_weeks_df["week"] = all_weeks_df["start_date"].dt.strftime("%U").astype(int)
        all_weeks_df["initial_year"] = all_weeks_df["start_date"].dt.year
        all_weeks_df["initial_month"] = all_weeks_df["start_date"].dt.month
        merged_df = pd.merge(all_weeks_df, df_sorted, how="left", on=["week", "initial_year"])

        merged_df["total_hectares"].fillna(0, inplace=True)
        merged_df = merged_df.drop(merged_df.loc[merged_df['week'] > 52].index)
        merged_df = merged_df.drop(merged_df.loc[merged_df['week'] < 1].index)
        df_result = merged_df.drop(['start_date_x', 'start_date_y'], axis=1)

        dict_from_df = df_result.to_dict(orient='records')
        return dict_from_df

    @staticmethod
    async def get_most_planted_crop_by_municipality(token: str, user_login: int) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_most_planted_crop_by_municipality(user_login)
            response = await WeeksStatisticsUseCase.purge_data_municipality_production(crops)
            return response

    @staticmethod
    async def purge_data_municipality_production(data: List[MunicipalityProductionModelOut]) -> List[dict]:
        df = pd.DataFrame([model.__dict__ for model in data])
        print(df)
        df_group = (df.groupby(['municipality_id', 'name_municipality', 'harvest_id',
                                'name_harvest', 'code_harvest'])['total_hectares'].sum().
                    reset_index())
        print(df_group)
        hectares_max = df_group.groupby('municipality_id')['total_hectares'].idxmax()
        print(hectares_max)
        df_group = df_group.loc[hectares_max]
        print(df_group)
        df_sorted = df_group.sort_values(by='total_hectares', ascending=False)
        dict_from_df = df_sorted.to_dict(orient='records')
        return dict_from_df

    @staticmethod
    async def most_widely_planted_crops(user_login: int, token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await CropUseCase.get_most_widely_planted_crops(user_login)
            df = pd.DataFrame([model.__dict__ for model in crops])
            df_group = (df.groupby(['harvest_id',
                                    'name_harvest', 'code_harvest'])['hectares'].sum().
                        reset_index())
            df_sorted = df_group.sort_values(by='hectares', ascending=False)
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

    @staticmethod
    async def home() -> dict:
        count_home = await UserUseCase.count_home()
        return {
            'count_users': count_home['count_users'],
            'count_harvests': count_home['count_harvests'],
            'count_municipalities': count_home['count_municipalities'],
            'count_hectares': round(count_home['count_hectares'], 2)
        }
