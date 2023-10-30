from typing import List
from abc import ABC, abstractmethod
from src.domain.models.country_model import CountryModelIn, CountryModelOut


class CountryRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_country(country: CountryModelIn) -> CountryModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_country_by_id(id_country: int) -> CountryModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_country(id_country: int, country: CountryModelIn) -> CountryModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_countries() -> List[CountryModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_country(id_country: int) -> None:
        pass
