from typing import List
from abc import ABC, abstractmethod
from src.domain.models.gender_model import GenderModelIn, GenderModelOut


class GenderRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_gender(gender: GenderModelIn) -> GenderModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_gender_by_id(id_gender: int) -> GenderModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_gender(id_gender: int, gender: GenderModelIn) -> GenderModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_genders() -> List[GenderModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_gender(id_gender: int) -> None:
        pass
