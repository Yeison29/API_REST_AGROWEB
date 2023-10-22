from typing import List
from abc import ABC, abstractmethod
from src.domain.models.user_model import UserModelIn, UserModelOut


class UserRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_user(user: UserModelIn) -> UserModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_user_by_id(id_user: int) -> UserModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_user(id_user: int, user: UserModelIn) -> UserModelIn:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_users() -> List[UserModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_user(id_user: int) -> None:
        pass
