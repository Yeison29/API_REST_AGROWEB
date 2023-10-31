from typing import List
from src.infrastructure.adapters.gender_repository_adapter import (GenderRepositoryAdapter, GenderModelOut,
                                                                   GenderModelIn)
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

gender_repository = GenderRepositoryAdapter


class GenderUseCase:

    @staticmethod
    async def add_gender(gender: GenderModelIn, token: str) -> GenderModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await gender_repository.add_gender(gender)
            return response

    @staticmethod
    async def get_gender_by_id(id_gender: int, token: str) -> GenderModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            gender = await gender_repository.get_gender_by_id(id_gender)
            return gender

    @staticmethod
    async def update_gender(id_gender: int, gender_update: GenderModelIn,  token: str) -> GenderModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_gender = await gender_repository.update_gender(id_gender, gender_update)
            return updated_gender

    @staticmethod
    async def get_all_genders() -> List[GenderModelOut]:
        genders = await gender_repository.get_all_genders()
        return genders

    @staticmethod
    async def delete_gender(id_gender: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_gender = await gender_repository.delete_gender(id_gender)
            return delete_gender
