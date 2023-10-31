from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.domain.models.authentication_model import (AuthenticationModel, AuthenticationModelIn, AuthenticationModelOut,
                                                    AuthenticationModelReceive)
from src.infrastructure.adapters.authentication_repository_adapter import AuthenticationRepositoryAdapter
from passlib.context import CryptContext
from src.domain.models.token_model import TokenModel

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
        response = await auth_repository.add_auth(auth_in)
        return response

    @staticmethod
    async def authenticate_user(plane_password: str, email_user: str) -> TokenModel:
        auth = await auth_repository.get_auth_by_email(email_user)
        if not password_context.verify(plane_password, auth.auth_password):
            raise HTTPException(status_code=401, detail="Could not validate credentials",
                                headers={"WWW-Authenticate": "Bearer"})
        access_token_expires = timedelta(minutes=60)
        access_token_jwt = await auth_repository.create_token({"sub": auth.auth_email_user}, access_token_expires)
        token = TokenModel(
            access_token=access_token_jwt,
            token_type="bearer"
        )
        return token

    @staticmethod
    async def update_auth(id_user: int, auth_email: str) -> AuthenticationModelOut:
        updated_auth = await auth_repository.update_auth(id_user, auth_email)
        return updated_auth

    @staticmethod
    async def form_data_to_authenticate_model_receive(form_data: OAuth2PasswordRequestForm = Depends()) -> (
            AuthenticationModelReceive):
        auth_model_receive = AuthenticationModelReceive(
            auth_email_user=form_data.username,
            auth_password=form_data.password
        )
        return auth_model_receive

    @staticmethod
    async def get_user_current(token: str) -> bool:
        auth = await auth_repository.get_user_current(token)
        return auth
