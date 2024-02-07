from typing import List
from src.infrastructure.adapters.harvest_repository_adapter import (HarvestRepositoryAdapter, HarvestModelIn,
                                                                    HarvestModelOut)
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

harvest_repository = HarvestRepositoryAdapter


class HarvestUseCase:

    @staticmethod
    async def add_harvest(harvest: HarvestModelIn, token: str) -> HarvestModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await harvest_repository.add_harvest(harvest)
            return response

    @staticmethod
    async def get_harvest_by_id(id_harvest: int, token: str) -> HarvestModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            harvest = await harvest_repository.get_harvest_by_id(id_harvest)
            return harvest

    @staticmethod
    async def update_harvest(id_harvest: int, harvest_update: HarvestModelIn,  token: str) -> HarvestModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_harvest = await harvest_repository.update_harvest(id_harvest, harvest_update)
            return updated_harvest

    @staticmethod
    async def get_all_harvests(user_login: int, token: str) -> List[HarvestModelOut]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            harvests = await harvest_repository.get_all_harvests(user_login)
            return harvests

    @staticmethod
    async def delete_harvest(id_harvest: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_harvest = await harvest_repository.delete_harvest(id_harvest)
            return delete_harvest

    @staticmethod
    async def count_harvests() -> int:
        count_harvests = await harvest_repository.count_harvests()
        return count_harvests
