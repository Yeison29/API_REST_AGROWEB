from typing import List
from src.domain.models.gender_model import GenderModelOut, GenderModelIn
from src.infrastructure.adapters.gender_repository_adapter import GenderRepositoryAdapter

user_repository = GenderRepositoryAdapter


class GenderUseCase:

    @staticmethod
    async def add_gender(gender: GenderModelIn):
        gender_db = await user_repository.add_gender(gender)
        print(gender_db)
        response = {
            **gender_db.dict()
        }
        return response

    @staticmethod
    async def get_gender(id_gender: int) -> GenderModelOut:
        gender = await user_repository.get_gender_by_id(id_gender)
        if not gender:
            raise ValueError("User not found")
        return GenderModelOut(**gender.dict())

    @staticmethod
    async def update_gender(id_gender: int, gender_update: GenderModelIn) -> GenderModelOut:
        user = await user_repository.get_gender_by_id(id_gender)
        if not user:
            raise ValueError("USER not found")

        updated_user = await user_repository.update_gender(id_gender, gender_update)
        return GenderModelOut(**updated_user.dict())

    @staticmethod
    async def get_all_genders() -> List[GenderModelOut]:
        genders = await user_repository.get_all_genders()
        return genders

    @staticmethod
    async def delete_gender(id_gender: int) -> None:
        user = await user_repository.get_gender_by_id(id_gender)
        if not user:
            raise ValueError("User not found")

        await user_repository.delete_gender(id_gender)
