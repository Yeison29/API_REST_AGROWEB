from typing import List
from fastapi import HTTPException
from src.domain.repositories.user_repository import UserRepository, UserModelIn, UserModelOut
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (UserEntity)


class UserRepositoryAdapter(UserRepository):

    @staticmethod
    async def add_user(user: UserModelIn) -> UserModelOut:
        new_user = UserEntity(name_user=user.name_user, lastname_user=user.lastname_user, email_user=user.email_user,
                              id_document_user=user.id_document_user, birthdate_user=user.birthdate_user,
                              phone_user=user.phone_user, type_document_id=user.type_document_id,
                              gender_id=user.gender_id, municipality_id=user.municipality_id)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        session.close()
        user_model_out = UserModelOut(
            id_user=new_user.id_user,
            name_user=new_user.name_user,
            lastname_user=new_user.lastname_user,
            phone_user=new_user.phone_user,
            email_user=new_user.email_user,
            id_document_user=new_user.id_document_user,
            birthdate_user=new_user.birthdate_user,
            type_document_id=new_user.type_document_id,
            gender_id=new_user.gender_id,
            municipality_id=user.municipality_id
        )
        return user_model_out

    @staticmethod
    async def get_user_by_id(id_user: int) -> UserModelOut:
        query = session.query(UserEntity).where(UserEntity.id_user == id_user).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="User not found")
        else:
            user_model_out = UserModelOut(
                id_user=query.id_user,
                name_user=query.name_user,
                lastname_user=query.lastname_user,
                phone_user=query.phone_user,
                email_user=query.id_document_user,
                id_document_user=query.id_document_user,
                birthdate_user=query.birthdate_user,
                type_document_id=query.type_document_id,
                gender_id=query.gender_id,
                municipality_id=query.municipality_id
            )
            session.commit()
            session.close()
            return user_model_out

    @staticmethod
    async def update_user(id_user: int, user: UserModelIn) -> UserModelOut:
        query = session.query(UserEntity).where(UserEntity.id_user == id_user).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="User not found")
        else:
            if query:
                for key, value in user.dict().items():
                    setattr(query, key, value)

        user_model_out = UserModelOut(
            id_user=id_user,
            name_user=user.name_user,
            lastname_user=user.lastname_user,
            phone_user=user.phone_user,
            email_user=user.id_document_user,
            id_document_user=user.id_document_user,
            birthdate_user=user.birthdate_user,
            type_document_id=user.type_document_id,
            gender_id=user.gender_id,
            municipality_id=user.municipality_id
        )
        session.commit()
        session.close()
        return user_model_out

    @staticmethod
    async def get_all_users() -> List[UserModelOut]:
        query = session.query(UserEntity).all()
        users_model_out_list = [
            UserModelOut(
                id_user=q.id_user,
                name_user=q.name_user,
                lastname_user=q.lastname_user,
                phone_user=q.phone_user,
                email_user=q.id_document_user,
                id_document_user=q.id_document_user,
                birthdate_user=q.birthdate_user,
                type_document_id=q.type_document_id,
                gender_id=q.gender_id,
                municipality_id=q.municipality_id
            )
            for q in query
        ]
        session.commit()
        session.close()
        return users_model_out_list

    @staticmethod
    async def delete_user(id_user: int) -> None:
        query = session.query(UserEntity).where(UserEntity.id_user == id_user).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="User not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None
