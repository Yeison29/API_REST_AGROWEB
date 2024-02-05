from abc import ABC
from typing import List, Union
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi_mail import FastMail, MessageSchema, MessageType
from src.infrastructure.adapters.data_sources.db_config import get_db_connection, psycopg2
from src.domain.repositories.authentication_repository import (AuthenticationRepository, AuthenticationModelOut,
                                                               AuthenticationModelIn, ActivateAccountModel,
                                                               AuthenticationModelOutToken)
from src.infrastructure.adapters.data_sources.email_config import conf
from src.infrastructure.adapters.data_sources.db_config import secret_key, algorithm
import json

oauth2_scheme = OAuth2PasswordBearer("/token")
connection = get_db_connection()


class AuthenticationRepositoryAdapter(AuthenticationRepository, ABC):

    @staticmethod
    async def get_auth_by_email(email_user: str) -> AuthenticationModelOutToken:
        data_query = ()
        print(email_user)
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM agro_web.get_auth_by_email(%s)", (email_user,))
            data_query = cursor.fetchall()
            connection.commit()
            cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)
            connection.rollback()
            raise HTTPException(status_code=400,
                                detail=f"Error: '{data_query[0][2]}'")
        print(data_query)
        if data_query[0][0] is False:
            raise HTTPException(status_code=400,
                                detail=f"Transaction error in DB: '{data_query[0][2]}'")
        response_json = json.loads(data_query[0][1])
        return AuthenticationModelOutToken(
            id_auth=response_json['id_auth'],
            auth_password=response_json['auth_password'],
            auth_email_user=response_json['auth_email'],
            auth_user_id=response_json['user_id'],
            auth_disabled=response_json['disabled_auth'],
            code_valid=response_json['code_valid'],
            name_user=response_json['name_user']
        )

    @staticmethod
    async def update_auth(id_user: int, auth_email: str) -> AuthenticationModelOut:
        # query = session.query(AuthenticationEntity).where(AuthenticationEntity.user_id == id_user).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Authentication not found")
        # else:
        #     if hasattr(query, 'email_user_auth'):
        #         setattr(query, 'email_user_auth', auth_email)
        #
        # auth_model_out = AuthenticationModelOut(
        #     id_auth=query.id_auth,
        #     auth_password=query.password_auth,
        #     auth_email_user=auth_email,
        #     auth_user_id=query.user_id,
        #     auth_disabled=query.disabled_auth,
        #     code_valid=query.code_valid
        # )
        # try:
        #     session.commit()
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a authentication with the email: {auth_email}")
        # return auth_model_out
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

    @staticmethod
    async def activate_account(activate_data: ActivateAccountModel) -> None:
        data_query = ()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM agro_web.activate_account(%s, %s)",
                           (activate_data.auth_id, activate_data.code))
            data_query = cursor.fetchall()
            connection.commit()
            cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)
            connection.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a user: {error}")
        print(data_query)
        if data_query[0][0] is False:
            raise HTTPException(status_code=400,
                                detail=f"Transaction error in DB: '{data_query[0][2]}'")

        # query = session.query(AuthenticationEntity).where(AuthenticationEntity.id_auth == activate_data.auth_id
        #                                                   and AuthenticationEntity.code_valid == activate_data.code
        #                                                   ).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Code error")
        # else:
        #     if hasattr(query, 'disabled_auth'):
        #         setattr(query, 'disabled_auth', False)
        #         raise HTTPException(status_code=200, detail="Account active")
        #
        # try:
        #     session.commit()
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"Error in activating the account")
        pass

    @staticmethod
    async def send_email(data_user: AuthenticationModelOut, name_user: str) -> None:
        html = f"""<div style="width: 100%; text-align: center;">
          <div style="margin: 5%;">
            <h1>¡Bienvenido<br />a<br /><span style="color: rgba(1,125,63,1);">AGRO</span>-<span
                style="color: rgb(241, 207, 105);">WEB</span>!</h1>
            <p style="color: black;">Querido <span style="text-transform: uppercase; font-weight: 700;">{name_user}</span>, 
            Estamos deseando que empieces. Primero tienes que confirmar tu cuenta. Haz clic en el botón de
              abajo.</p>
          </div>
          <a href="http://127.0.0.1:8000/api/activate/{data_user.id_auth}+{data_user.code_valid}" class="btn"
            style="text-decoration: none; color: #fff; background-color: rgba(1,125,63,1); padding: 20px; cursor: pointer; border-radius: 10px;">Click
            para activar</a>
          <div style="margin: 5%;">
            <p style="color: black;">Si no puedes hacer clic en el enlace, cópialo y pégalo en la barra de direcciones de tu
              navegador.</p>
            <a href="http://127.0.0.1:8000/api/activate/{data_user.id_auth}+{data_user.code_valid}">http://127.0.0.1:8000/api/activate/{data_user.id_auth}+{data_user.code_valid}</a>
          </div>
          <p>Una vez que hayas completado estos pasos, tu registro estará confirmado y podrás acceder a todos los servicios de
            <span style="color: rgba(1,125,63,1);">AGRO</span>-<span style="color: rgb(241, 207, 105);">WEB</span></p>
          <div style="margin: 5%;">
            <h3>¡Gracias por unirte a nosotros!</h3>
          </div>
        </div>"""

        message = MessageSchema(
            subject="Activar cuenta de AGRO-WEB",
            recipients=[data_user.auth_email_user],
            body=html,
            subtype=MessageType.html)

        fm = FastMail(conf)
        await fm.send_message(message)
