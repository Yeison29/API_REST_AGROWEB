from typing import List
from abc import ABC, abstractmethod
from src.domain.models.crop_model import CropModelIn, CropModelOut, CropModelOut2
from src.domain.models.municipality_production_model import MunicipalityProductionModelOut


class CropRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_crop(gender: CropModelIn) -> CropModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_crop_by_id(id_crop: int) -> CropModelOut2:
        pass

    @staticmethod
    @abstractmethod
    async def update_crop(id_crop: int, crop: CropModelIn) -> CropModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_crops(user_id: int) -> List[CropModelOut2]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_crop(id_crop: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_crops_harvest_by_id(harvest_id: int) -> List[CropModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_crops_past() -> List[MunicipalityProductionModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def get_most_widely_planted_crops() -> List[CropModelOut2]:
        pass

    @staticmethod
    @abstractmethod
    async def count_hectares() -> int:
        pass
