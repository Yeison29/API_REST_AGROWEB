from typing import List
from abc import ABC, abstractmethod
from src.domain.models.gender_model import GenderModelIn, GenderModelOut, GenderModelUpdate


class GenderRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_gender(gender: GenderModelIn) -> GenderModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_gender_by_id(gender_id: int) -> GenderModelIn:
        pass

    @staticmethod
    @abstractmethod
    async def update_gender(gender_id: int, gender: GenderModelIn) -> GenderModelIn:
        pass

    @staticmethod
    @abstractmethod
    async def get_gender() -> List[GenderModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_gender(gender_id: int) -> None:
        pass
