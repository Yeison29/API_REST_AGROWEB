from typing import List, Union
from datetime import timedelta
from abc import ABC, abstractmethod
from src.domain.models.authentication_model import AuthenticationModelIn, AuthenticationModelOut
from src.domain.models.token_model import TokenModel


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
    async def delete_auth(id_auth: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def create_token(data: dict, time_expire: Union[timedelta, None] = None) -> str:
        pass

    @staticmethod
    @abstractmethod
    async def get_user_current(token: TokenModel) -> bool:
        pass