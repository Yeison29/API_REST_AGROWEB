from typing import List
from src.domain.models.authentication_model import AuthenticationModel, AuthenticationModelIn, AuthenticationModelOut
from src.infrastructure.adapters.authentication_repository_adapter import AuthenticationRepositoryAdapter
from passlib.context import CryptContext

auth_repository = AuthenticationRepositoryAdapter
password_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


class AuthenticationUseCase:

    @staticmethod
    async def add_auth(user_id: int, auth_email_user: str, auth: AuthenticationModel) -> AuthenticationModelOut:
        password_hashed = password_context.hash(auth.auth_password)
        auth_in = AuthenticationModelIn(
            auth_password=password_hashed,
            auth_email_user=auth_email_user,
            auth_user_id=user_id,
            auth_disabled=False
        )
        print(auth_in)
        response = await auth_repository.add_auth(auth_in)
        return response
