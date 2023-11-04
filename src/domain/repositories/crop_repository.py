from typing import List
from abc import ABC, abstractmethod
from src.domain.models.crop_model import CropModelIn, CropModelOut


class CropRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_crop(gender: CropModelIn) -> CropModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_crop_by_id(id_crop: int) -> CropModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_crop(id_crop: int, crop: CropModelIn) -> CropModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_crops() -> List[CropModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_crop(id_crop: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def gat_all_crops_harvest_by_id(harvest_id: int) -> List[CropModelOut]:
        pass
