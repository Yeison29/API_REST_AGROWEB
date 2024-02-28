from typing import List
from src.infrastructure.adapters.municipality_repository_adapter import (MunicipalityRepositoryAdapter,
                                                                         MunicipalityModelOut, MunicipalityModelIn)
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

municipality_repository = MunicipalityRepositoryAdapter


class MunicipalityUseCase:

    @staticmethod
    async def add_municipality(municipality: MunicipalityModelIn, token: str) -> MunicipalityModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await municipality_repository.add_municipality(municipality)
            return response

    @staticmethod
    async def get_municipality_by_id(id_municipality: int, token: str) -> MunicipalityModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            municipality = await municipality_repository.get_municipality_by_id(id_municipality)
            return municipality

    @staticmethod
    async def update_municipality(id_municipality: int, municipality_update: MunicipalityModelIn, token: str) -> (
            MunicipalityModelOut):
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_municipality = await municipality_repository.update_municipality(id_municipality, municipality_update)
            return updated_municipality

    @staticmethod
    async def get_all_municipalities() -> List[MunicipalityModelOut]:
        municipalities = await municipality_repository.get_all_municipalities()
        return municipalities

    @staticmethod
    async def delete_municipality(id_municipality: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_municipality = await municipality_repository.delete_municipality(id_municipality)
            return delete_municipality

    @staticmethod
    async def count_municipalities() -> int:
        count_municipalities = await municipality_repository.count_municipalities()
        return count_municipalities
