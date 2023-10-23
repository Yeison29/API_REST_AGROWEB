from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
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
        print(password_hashed)
        auth_in = AuthenticationModelIn(
            auth_password=password_hashed,
            auth_email_user=auth_email_user,
            auth_user_id=user_id,
            auth_disabled=False
        )
        print(auth_in)
        response = await auth_repository.add_auth(auth_in)
        return response

    @staticmethod
    async def authenticate_user(plane_password: str, email_user: str) -> TokenModel:
        auth = await auth_repository.get_auth_by_email(email_user)
        print(auth)
        if not password_context.verify(plane_password, auth.auth_password):
            raise HTTPException(status_code=401, detail="Could not validate credentials",
                                headers={"WWW-Authenticate": "Bearer"})
        token = TokenModel(
            access_token="HELLO WORD!",
            token_type="bearer"
        )
        return token

    @staticmethod
    async def form_data_to_authenticate_model_receive(form_data: OAuth2PasswordRequestForm = Depends()) -> (
            AuthenticationModelReceive):
        print(form_data)
        auth_model_receive = AuthenticationModelReceive(
            auth_email_user=form_data.username,
            auth_password=form_data.password
        )
        return auth_model_receive
