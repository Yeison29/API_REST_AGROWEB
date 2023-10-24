from typing import List
from src.domain.models.gender_model import GenderModelOut, GenderModelIn
from src.infrastructure.adapters.gender_repository_adapter import GenderRepositoryAdapter
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

user_repository = GenderRepositoryAdapter


class GenderUseCase:

    @staticmethod
    async def add_gender(gender: GenderModelIn, token: str) -> GenderModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await user_repository.add_gender(gender)
            return response

    @staticmethod
    async def get_gender(id_gender: int, token: str) -> GenderModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            gender = await user_repository.get_gender_by_id(id_gender)
            if not gender:
                raise ValueError("User not found")
            return GenderModelOut(**gender.dict())

    @staticmethod
    async def update_gender(id_gender: int, gender_update: GenderModelIn,  token: str) -> GenderModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            user = await user_repository.get_gender_by_id(id_gender)
            if not user:
                raise ValueError("USER not found")

            updated_user = await user_repository.update_gender(id_gender, gender_update)
            return GenderModelOut(**updated_user.dict())

    @staticmethod
    async def get_all_genders(token: str) -> List[GenderModelOut]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            genders = await user_repository.get_all_genders()
            return genders

    @staticmethod
    async def delete_gender(id_gender: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            user = await user_repository.get_gender_by_id(id_gender)
            if not user:
                raise ValueError("User not found")

            await user_repository.delete_gender(id_gender)
