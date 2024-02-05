from typing import List
from src.infrastructure.adapters.user_repository_adapter import (UserRepositoryAdapter, UserModelOut, UserModelIn,
                                                                 UserModelAuthIn)
from src.domain.uses_cases.authentication_use_cases import (AuthenticationUseCase, AuthenticationModel,
                                                            AuthenticationRepositoryAdapter, AuthenticationModelOut)
from passlib.context import CryptContext
import secrets

user_repository = UserRepositoryAdapter
auth_repository = AuthenticationRepositoryAdapter
password_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


class UserUseCase:

    @staticmethod
    async def add_user(user: UserModelIn, auth: AuthenticationModel) -> UserModelOut:
        password_hashed = password_context.hash(auth.auth_password)
        code = secrets.token_hex(2)[:4]
        user_auth_in = UserModelAuthIn(
            name_user=user.name_user,
            lastname_user=user.lastname_user,
            email_user=user.email_user,
            phone_user=user.phone_user,
            id_document_user=user.id_document_user,
            birthdate_user=user.birthdate_user,
            type_document_id=user.type_document_id,
            gender_id=user.gender_id,
            municipality_id=user.municipality_id,
            auth_password=password_hashed,
            code_valid=code
        )
        # response = await auth_repository.add_auth(auth_in)
        # await AuthenticationUseCase.send_email(response, name_user)
        user_db = await user_repository.add_user(user_auth_in)
        auth_model_out = AuthenticationModelOut(
            id_auth=user_db.id_auth,
            auth_email_user=user_db.email_user,
            auth_password=user_db.auth_password,
            auth_disabled=True,
            auth_user_id=user_db.id_user,
            code_valid=user_db.code_valid
        )
        await AuthenticationUseCase.send_email(auth_model_out, user_db.name_user)
        auth_model_out = None
        user_db = UserModelOut(
            name_user=user_db.name_user,
            lastname_user=user_db.lastname_user,
            email_user=user_db.email_user,
            phone_user=user_db.phone_user,
            id_document_user=user_db.id_document_user,
            birthdate_user=user_db.birthdate_user,
            type_document_id=user_db.type_document_id,
            gender_id=user_db.gender_id,
            municipality_id=user_db.municipality_id,
            id_user=user_db.id_user
        )
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

    @staticmethod
    async def statistics_genres() -> List[UserModelOut]:
        users = await user_repository.statistics_genres()
        return users

    @staticmethod
    async def age_renge() -> List[UserModelOut]:
        ages = await user_repository.age_range()
        return ages

    @staticmethod
    async def count_users() -> int:
        count_users = await user_repository.count_users()
        return count_users
