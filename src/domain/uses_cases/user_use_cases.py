from typing import List
from src.domain.models.authentication_model import AuthenticationModel
from src.infrastructure.adapters.user_repository_adapter import UserRepositoryAdapter, UserModelOut, UserModelIn
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

user_repository = UserRepositoryAdapter


class UserUseCase:

    @staticmethod
    async def add_user(user: UserModelIn, auth: AuthenticationModel) -> UserModelOut:
        user_db = await user_repository.add_user(user)
        await AuthenticationUseCase.add_auth(user_db.id_user, user_db.email_user, auth)
        return user_db

    @staticmethod
    async def get_user_by_id(id_user: int, token: str) -> UserModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            user = await user_repository.get_user_by_id(id_user)
            return user

    @staticmethod
    async def update_user(id_user: int, user_update: UserModelIn, token: str) -> UserModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_user = await user_repository.update_user(id_user, user_update)
            await AuthenticationUseCase.update_auth(id_user, user_update.email_user)
            return updated_user

    @staticmethod
    async def get_all_users(token: str) -> List[UserModelOut]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            users = await user_repository.get_all_users()
            return users

    @staticmethod
    async def delete_user(id_user: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_user = await user_repository.delete_user(id_user)
            return delete_user
