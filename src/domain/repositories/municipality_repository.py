from typing import List
from abc import ABC, abstractmethod
from src.domain.models.municipality_model import MunicipalityModelOut, MunicipalityModelIn


class MunicipalityRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_municipality(municipality: MunicipalityModelIn) -> MunicipalityModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_municipality_by_id(id_municipality: int) -> MunicipalityModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_municipality(id_municipality: int, municipality: MunicipalityModelIn) -> MunicipalityModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_municipalities(id_department: int) -> List[MunicipalityModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_municipality(id_municipality: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def count_municipalities() -> int:
        pass
