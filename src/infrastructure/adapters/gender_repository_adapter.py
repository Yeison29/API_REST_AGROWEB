from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.domain.repositories.gender_repository import GenderRepository, GenderModelIn, GenderModelOut
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (GenderEntity)


class GenderRepositoryAdapter(GenderRepository):

    @staticmethod
    async def add_gender(gender: GenderModelIn) -> GenderModelOut:
        new_gender = GenderEntity(name_gender=gender.name_gender, code_gender=gender.code_gender)
        session.add(new_gender)
        try:
            session.commit()
            session.refresh(new_gender)
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a gender with the code: {gender.code_gender}")
        gender_model_out = GenderModelOut(
            id_gender=new_gender.id_gender,
            name_gender=new_gender.name_gender,
            code_gender=new_gender.code_gender
        )
        return gender_model_out

    @staticmethod
    async def get_gender_by_id(id_gender: int) -> GenderModelOut:
        query = session.query(GenderEntity).where(GenderEntity.id_gender == id_gender).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Gender not found")
        else:
            gender_model_out = GenderModelOut(
                id_gender=query.id_gender,
                name_gender=query.name_gender,
                code_gender=query.code_gender
            )
            session.commit()
            session.close()
            return gender_model_out

    @staticmethod
    async def update_gender(id_gender: int, gender: GenderModelIn) -> GenderModelOut:
        query = session.query(GenderEntity).where(GenderEntity.id_gender == id_gender).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Gender not found")
        else:
            if query:
                for key, value in gender.dict().items():
                    setattr(query, key, value)

        gender_model_out = GenderModelOut(
            id_gender=id_gender,
            name_gender=gender.name_gender,
            code_gender=gender.code_gender
        )
        try:
            session.commit()
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a gender with the code: {gender.code_gender}")
        return gender_model_out

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
    async def delete_gender(id_gender: int) -> None:
        query = session.query(GenderEntity).where(GenderEntity.id_gender == id_gender).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Gender not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None
