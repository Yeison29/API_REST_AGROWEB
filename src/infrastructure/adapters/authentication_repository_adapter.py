from typing import List
from src.domain.models.authentication_model import AuthenticationModelOut, AuthenticationModelIn
from src.domain.repositories.authentication_repository import AuthenticationRepository
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (AuthenticationEntity)


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
    async def get_auth_by_id(auth: int) -> AuthenticationModelOut:
        pass

    @staticmethod
    async def update_auth(id_auth: int, auth: AuthenticationModelIn) -> AuthenticationModelIn:
        pass

    @staticmethod
    async def get_all_auths() -> List[AuthenticationModelOut]:
        pass

    @staticmethod
    async def auth_user(id_auth: int) -> None:
        pass
