from typing import List
from abc import ABC, abstractmethod
from src.domain.models.authentication_model import AuthenticationModelIn, AuthenticationModelOut, AuthenticationModelUpdate


class AuthenticationRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_auth(auth: AuthenticationModelIn) -> AuthenticationModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_auth_by_email(email_user: str) -> AuthenticationModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_auth(id_auth: int, auth: AuthenticationModelIn) -> AuthenticationModelIn:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_auths() -> List[AuthenticationModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def auth_user(id_auth: int) -> None:
        pass
