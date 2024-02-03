from abc import ABC
from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.domain.repositories.user_repository import (UserRepository, UserModelOut, UserModelOut2,
                                                     UserModelAuthIn, UserModelIn, UserModelAuthOut)
from src.infrastructure.adapters.data_sources.db_config import get_db_connection, psycopg2


class UserRepositoryAdapter(UserRepository, ABC):

    @staticmethod
    async def add_user(user_auth_in: UserModelAuthIn) -> UserModelAuthOut:
        data_query = ()
        try:
            cursor = get_db_connection().cursor()
            cursor.execute("SELECT * FROM agro_web.create_user_agroweb(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (user_auth_in.name_user, user_auth_in.lastname_user, user_auth_in.email_user,
                            user_auth_in.phone_user, user_auth_in.id_document_user, user_auth_in.birthdate_user,
                            user_auth_in.type_document_id, user_auth_in.gender_id, user_auth_in.municipality_id,
                            user_auth_in.auth_password, user_auth_in.code_valid))
            data_query = cursor.fetchall()
            cursor.commit()
            cursor.close()
        except psycopg2.DatabaseError as error:
            get_db_connection().rollback()
            print(error)
            raise HTTPException(status_code=400,
                                detail=f"There is already a user: {error}")

        print(data_query)
        return UserModelAuthOut(
            # name_user=user_auth_in.name_user,
            # lastname_user=user_auth_in.lastname_user,
            # email_user=user_auth_in.email_user,
            # phone_user=user_auth_in.phone_user,
            # id_document_user=user_auth_in.id_document_user,
            # birthdate_user=user_auth_in.birthdate_user,
            # type_document_id=user_auth_in.type_document_id,
            # gender_id=user_auth_in.gender_id,
            # municipality_id=user_auth_in.municipality_id,
            # user_id=data_query.
        )

        # new_user = UserEntity(name_user=user.name_user, lastname_user=user.lastname_user, email_user=user.email_user,
        #                       id_document_user=user.id_document_user, birthdate_user=user.birthdate_user,
        #                       phone_user=user.phone_user, type_document_id=user.type_document_id,
        #                       gender_id=user.gender_id, municipality_id=user.municipality_id)
        # session.add(new_user)
        # try:
        #     session.commit()
        #     session.refresh(new_user)
        #     session.close()
        # except IntegrityError as e:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a user: {e}")
        # user_model_out = UserModelOut(
        #     id_user=new_user.id_user,
        #     name_user=new_user.name_user,
        #     lastname_user=new_user.lastname_user,
        #     phone_user=new_user.phone_user,
        #     email_user=new_user.email_user,
        #     id_document_user=new_user.id_document_user,
        #     birthdate_user=new_user.birthdate_user,
        #     type_document_id=new_user.type_document_id,
        #     gender_id=new_user.gender_id,
        #     municipality_id=user.municipality_id
        # )
        # return user_model_out
        pass

    @staticmethod
    async def get_user_by_id(id_user: int) -> UserModelOut:
        # query = session.query(UserEntity).where(UserEntity.id_user == id_user).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="User not found")
        # else:
        #     user_model_out = UserModelOut(
        #         id_user=query.id_user,
        #         name_user=query.name_user,
        #         lastname_user=query.lastname_user,
        #         phone_user=query.phone_user,
        #         email_user=query.email_user,
        #         id_document_user=query.id_document_user,
        #         birthdate_user=query.birthdate_user,
        #         type_document_id=query.type_document_id,
        #         gender_id=query.gender_id,
        #         municipality_id=query.municipality_id
        #     )
        #     session.commit()
        #     session.close()
        #     return user_model_out
        pass

    @staticmethod
    async def update_user(id_user: int, user: UserModelIn) -> UserModelOut:
        # query = session.query(UserEntity).where(UserEntity.id_user == id_user).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="User not found")
        # else:
        #     if query:
        #         for key, value in user.dict().items():
        #             setattr(query, key, value)
        #
        # user_model_out = UserModelOut(
        #     id_user=id_user,
        #     name_user=user.name_user,
        #     lastname_user=user.lastname_user,
        #     phone_user=user.phone_user,
        #     email_user=user.email_user,
        #     id_document_user=user.id_document_user,
        #     birthdate_user=user.birthdate_user,
        #     type_document_id=user.type_document_id,
        #     gender_id=user.gender_id,
        #     municipality_id=user.municipality_id
        # )
        # try:
        #     session.commit()
        #     session.close()
        # except IntegrityError as e:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a user: {e}")
        # return user_model_out
        pass

    @staticmethod
    async def get_all_users() -> List[UserModelOut]:
        # query = session.query(UserEntity).all()
        # users_model_out_list = [
        #     UserModelOut(
        #         id_user=q.id_user,
        #         name_user=q.name_user,
        #         lastname_user=q.lastname_user,
        #         phone_user=q.phone_user,
        #         email_user=q.email_user,
        #         id_document_user=q.id_document_user,
        #         birthdate_user=q.birthdate_user,
        #         type_document_id=q.type_document_id,
        #         gender_id=q.gender_id,
        #         municipality_id=q.municipality_id
        #     )
        #     for q in query
        # ]
        # session.commit()
        # session.close()
        # return users_model_out_list
        pass

    @staticmethod
    async def delete_user(id_user: int) -> None:
        # query = session.query(UserEntity).where(UserEntity.id_user == id_user).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="User not found")
        # else:
        #     if query:
        #         session.delete(query)
        #     session.commit()
        #     session.close()
        # return None
        pass

    @staticmethod
    async def statistics_genres() -> List[UserModelOut2]:
        # query = (
        #     session.query(UserEntity, GenderEntity, AuthenticationEntity.disabled_auth)
        #     .join(GenderEntity, UserEntity.gender_id == GenderEntity.id_gender)
        #     .filter(~AuthenticationEntity.disabled_auth)
        #     .all()
        # )
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        # else:
        #     result = [
        #         UserModelOut2(
        #             id_user=UserEntity.id_user,
        #             name_user=UserEntity.name_user,
        #             lastname_user=UserEntity.lastname_user,
        #             phone_user=UserEntity.phone_user,
        #             email_user=UserEntity.email_user,
        #             id_document_user=UserEntity.id_document_user,
        #             birthdate_user=UserEntity.birthdate_user,
        #             type_document_id=UserEntity.type_document_id,
        #             gender_id=UserEntity.gender_id,
        #             municipality_id=UserEntity.municipality_id,
        #             name_gender=GenderEntity.name_gender,
        #             code_gender=GenderEntity.code_gender
        #         )
        #         for UserEntity, GenderEntity, auth in query
        #     ]
        #     session.commit()
        #     session.close()
        #     return result
        pass

    @staticmethod
    async def age_range() -> List[UserModelOut]:
        # query = (
        #     session.query(UserEntity, AuthenticationEntity.disabled_auth)
        #     .filter(~AuthenticationEntity.disabled_auth)
        #     .all()
        # )
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        # else:
        #     users_model_out_list = [
        #         UserModelOut(
        #             id_user=q.id_user,
        #             name_user=q.name_user,
        #             lastname_user=q.lastname_user,
        #             phone_user=q.phone_user,
        #             email_user=q.email_user,
        #             id_document_user=q.id_document_user,
        #             birthdate_user=q.birthdate_user,
        #             type_document_id=q.type_document_id,
        #             gender_id=q.gender_id,
        #             municipality_id=q.municipality_id
        #         )
        #         for q, auth in query
        #     ]
        #     session.commit()
        #     session.close()
        #     return users_model_out_list
        pass

    @staticmethod
    async def count_users() -> int:
        # count_users = session.query(UserEntity).count()
        # return count_users
        pass
