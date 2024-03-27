from typing import List
from src.infrastructure.adapters.country_repository_adapter import (CountryRepositoryAdapter, CountryModelOut,
                                                                    CountryModelIn)
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

country_repository = CountryRepositoryAdapter


class CountryUseCase:

    @staticmethod
    async def add_country(country: CountryModelIn, token: str) -> CountryModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await country_repository.add_country(country)
            return response

    @staticmethod
    async def get_country_by_id(id_country: int, token: str) -> CountryModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            country = await country_repository.get_country_by_id(id_country)
            return country

    @staticmethod
    async def update_country(id_country: int, country_update: CountryModelIn,  token: str) -> CountryModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_country = await update_country(id_country, country_update)
            return updated_country

    @staticmethod
    async def get_all_countries() -> List[CountryModelOut]:
        countries = await country_repository.get_all_countries()
        return countries

    @staticmethod
    async def delete_country(id_country: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_country = await country_repository.delete_country(id_country)
            return delete_country
