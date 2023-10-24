from fastapi import Depends
from src.domain.models.token_model import TokenModel
from src.domain.models.user_model import UserModelIn
from src.domain.models.gender_model import GenderModelIn
from src.domain.models.authentication_model import AuthenticationModel
from src.domain.uses_cases.user_use_cases import UserUseCase
from src.domain.uses_cases.gender_use_cases import GenderUseCase
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer("/token")
user_use_case = UserUseCase()
gender_use_case = GenderUseCase()


class ApiRest:

    @staticmethod
    async def token(form_data: OAuth2PasswordRequestForm = Depends()):
        response = await AuthenticationUseCase.authenticate_user(form_data.password, form_data.username)
        return response

    @staticmethod
    async def add_user(user: UserModelIn, auth: AuthenticationModel, token: str = Depends(oauth2_scheme)):
        response = await user_use_case.add_user(user, auth, token)
        return response

    @staticmethod
    async def get_all_users(token: str = Depends(oauth2_scheme)):
        response = await user_use_case.get_all_users(token)
        return response

    @staticmethod
    async def get_user_by_id(id_user: int,  token: str = Depends(oauth2_scheme)):
        response = await user_use_case.get_user_by_id(id_user, token)
        return response

    @staticmethod
    async def update_user(id_user: int, user: UserModelIn, token: str = Depends(oauth2_scheme)):
        response = await user_use_case.update_user(id_user, user, token)
        return response

    @staticmethod
    async def delete_user(id_user: int, token: str = Depends(oauth2_scheme)):
        response = await user_use_case.delete_user(id_user, token)
        return response

    @staticmethod
    async def add_gender(gender: GenderModelIn,  token: str = Depends(oauth2_scheme)):
        response = await gender_use_case.add_gender(gender, token)
        return response

    @staticmethod
    async def get_all_genders(token: str = Depends(oauth2_scheme)):
        response = await gender_use_case.get_all_genders(token)
        return response
