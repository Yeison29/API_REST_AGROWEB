from typing import List
from src.domain.models.gender_model import GenderModelIn, GenderModelOut, GenderModelUpdate
from src.domain.repositories.gender_repository import GenderRepository
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (UserEntity, GenderEntity)


class GenderRepositoryAdapter(GenderRepository):

    @staticmethod
    async def add_gender(gender: GenderModelIn) -> GenderModelOut:
        new_gender = GenderEntity(name_gender=gender.name_gender, code_gender=gender.code_gender)
        session.add(new_gender)
        session.commit()
        session.refresh(new_gender)
        session.close()
        gender_model_out = GenderModelOut(
            id_gender=new_gender.id_gender,
            name_gender=new_gender.name_gender,
            code_gender=new_gender.code_gender
        )
        return gender_model_out

    @staticmethod
    async def get_gender_by_id(gender_id: int) -> GenderModelIn:
        query = UserEntity.user_table.select(UserEntity.user_table.c.id_user == user_id)
        return await database.fetch_one(query=query)

    @staticmethod
    async def update_gender(gender_id: int, gender: GenderModelIn) -> GenderModelIn:
        query = (
            UserEntity.user_table
            .update()
            .where(UserEntity.user_table.c.id_user == user_id)
            .values(**user.dict())
        )
        return await database.execute(query=query)

    @staticmethod
    async def get_all_genders() -> List[GenderModelOut]:
        query = session.query(GenderEntity).all()
        genders_model_out_list = [
            GenderModelOut(
                id_gender=q.id_gender,
                name_gender=q.name_gender,
                code_gender=q.code_gender
            )
            for q in query
        ]
        session.commit()
        session.close()
        return genders_model_out_list

    @staticmethod
    async def delete_gender(user_id: int) -> None:
        query = UserEntity.user_table.delete().where(UserEntity.user_table.c.id == id)
        return await database.execute(query=query)
