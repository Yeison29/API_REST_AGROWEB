from typing import List
from src.infrastructure.adapters.crop_repository_adapter import CropRepositoryAdapter, CropModelIn, CropModelOut
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

crop_repository = CropRepositoryAdapter


class CropUseCase:

    @staticmethod
    async def add_crop(crop: CropModelIn, token: str) -> CropModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await crop_repository.add_crop(crop)
            return response

    @staticmethod
    async def get_crop_by_id(id_crop: int, token: str) -> CropModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crop = await crop_repository.get_crop_by_id(id_crop)
            return crop

    @staticmethod
    async def update_crop(id_crop: int, crop_update: CropModelIn,  token: str) -> CropModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_crop = await crop_repository.update_crop(id_crop, crop_update)
            return updated_crop

    @staticmethod
    async def get_all_crops(token: str) -> List[CropModelOut]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            crops = await crop_repository.get_all_crops()
            return crops

    @staticmethod
    async def delete_crop(id_crop: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_crop = await crop_repository.delete_crop(id_crop)
            return delete_crop

    @staticmethod
    async def get_all_crops_harvest_by_id(harvest_id: int) -> List[CropModelOut]:
        crops = await crop_repository.gat_all_crops_harvest_by_id(harvest_id)
        return crops
