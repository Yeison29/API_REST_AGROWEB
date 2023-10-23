from src.domain.models.user_model import UserModelIn
from src.domain.models.gender_model import GenderModelIn
from src.domain.models.authentication_model import AuthenticationModel
from src.domain.uses_cases.user_use_cases import UserUseCase
from src.domain.uses_cases.gender_use_cases import GenderUseCase

user_use_case = UserUseCase()
gender_use_case = GenderUseCase()


class ApiRest:

    @staticmethod
    async def root():
        return {"message": "Hello World"}

    @staticmethod
    async def add_user(user: UserModelIn, auth: AuthenticationModel):
        response = await user_use_case.add_user(user, auth)
        return response

    @staticmethod
    async def get_all_users():
        response = await user_use_case.get_all_users()
        return response

    @staticmethod
    async def get_user_by_id(id_user: int):
        response = await user_use_case.get_user_by_id(id_user)
        return response

    @staticmethod
    async def update_user(id_user: int, user: UserModelIn):
        response = await user_use_case.update_user(id_user, user)
        return response

    @staticmethod
    async def delete_user(id_user: int):
        response = await user_use_case.delete_user(id_user)
        return response

    @staticmethod
    async def add_gender(gender: GenderModelIn):
        response = await gender_use_case.add_gender(gender)
        return response

    @staticmethod
    async def get_all_genders():
        response = await gender_use_case.get_all_genders()
        return response
