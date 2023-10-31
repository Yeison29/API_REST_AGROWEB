from typing import List
from abc import ABC, abstractmethod
from src.domain.models.harvest_model import HarvestModelOut, HarvestModelIn


class HarvestRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_harvest(harvest: HarvestModelIn) -> HarvestModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_harvest_by_id(id_harvest: int) -> HarvestModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_harvest(id_harvest: int, harvest: HarvestModelIn) -> HarvestModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_harvests() -> List[HarvestModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_harvest(id_harvest: int) -> None:
        pass
