from typing import List, Union
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from src.domain.models.authentication_model import AuthenticationModelOut, AuthenticationModelIn
from src.domain.repositories.authentication_repository import AuthenticationRepository
from src.infrastructure.adapters.data_sources.db_config import session, algorithm, secret_key
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (AuthenticationEntity)

oauth2_scheme = OAuth2PasswordBearer("/token")


class AuthenticationRepositoryAdapter(AuthenticationRepository):

    @staticmethod
    async def add_auth(auth: AuthenticationModelIn) -> AuthenticationModelOut:
        new_auth = AuthenticationEntity(email_user_auth=auth.auth_email_user, password_auth=auth.auth_password,
                                        disabled_auth=auth.auth_disabled, user_id=auth.auth_user_id)
        session.add(new_auth)
        session.commit()
        session.refresh(new_auth)
        session.close()
        auth_model_out = AuthenticationModelOut(
            id_auth=new_auth.id_auth,
            auth_email_user=new_auth.email_user_auth,
            auth_password=new_auth.password_auth,
            auth_disabled=new_auth.disabled_auth,
            auth_user_id=new_auth.user_id
        )
        return auth_model_out

    @staticmethod
    async def get_auth_by_email(email_user: str) -> AuthenticationModelOut:
        query = session.query(AuthenticationEntity).where(AuthenticationEntity.email_user_auth == email_user).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=401, detail="Could not validate credentials",
                                headers={"WWW-Authenticate": "Bearer"})
        else:
            auth_model_out = AuthenticationModelOut(
                id_auth=query.id_auth,
                auth_password=query.password_auth,
                auth_email_user=query.email_user_auth,
                auth_user_id=query.user_id,
                auth_disabled=query.disabled_auth
            )
            session.commit()
            session.close()
            return auth_model_out

    @staticmethod
    async def update_auth(id_auth: int, auth: AuthenticationModelIn) -> AuthenticationModelIn:
        pass

    @staticmethod
    async def get_all_auths() -> List[AuthenticationModelOut]:
        pass

    @staticmethod
    async def delete_auth(id_auth: int) -> None:
        pass

    @staticmethod
    async def create_token(data: dict, time_expire: Union[timedelta, None] = None) -> str:
        data_copy = data.copy()
        if time_expire is None:
            expires = datetime.utcnow() + timedelta(minutes=20)
        else:
            expires = datetime.utcnow() + time_expire
        data_copy.update({"exp": expires})
        token_jwt = jwt.encode(data_copy, key=secret_key, algorithm=algorithm)
        return token_jwt

    @staticmethod
    async def get_user_current(token: str) -> bool:
        try:
            token_decode = jwt.decode(token, key=secret_key, algorithms=[algorithm])
            user_email = token_decode.get("sub")
            if user_email is None:
                raise HTTPException(status_code=401, detail="Could not validate credentials",
                                    headers={"WWW-Authenticate": "Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="Could not validate credentials",
                                headers={"WWW-Authenticate": "Bearer"})
        auth = await AuthenticationRepositoryAdapter.get_auth_by_email(user_email)
        if not auth:
            raise HTTPException(status_code=400, detail="User not found",
                                headers={"WWW-Authenticate": "Bearer"})
        return True
