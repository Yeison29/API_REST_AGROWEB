from typing import List
from src.domain.models.user_model import UserModelOut, UserModelIn, UserModelUpdate
from src.infrastructure.adapters.user_repository_adapter import UserRepositoryAdapter

user_repository = UserRepositoryAdapter


class UserUseCase:

    @staticmethod
    async def add_user(user: UserModelIn):
        user_db = await user_repository.add_user(user)
        return user_db

    @staticmethod
    async def get_user_by_id(id_user: int) -> UserModelOut:
        user = await user_repository.get_user_by_id(id_user)
        return user

    @staticmethod
    async def update_user(id_user: int, user_update: UserModelIn) -> UserModelOut:
        updated_user = await user_repository.update_user(id_user, user_update)
        return updated_user

    @staticmethod
    async def get_all_users() -> List[UserModelOut]:
        users = await user_repository.get_all_users()
        return users

    @staticmethod
    async def delete_user(id_user: int) -> None:
        delete_user = await user_repository.delete_user(id_user)
        return delete_user
