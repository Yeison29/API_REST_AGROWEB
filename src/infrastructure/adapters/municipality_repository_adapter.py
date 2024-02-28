from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.domain.repositories.municipality_repository import (MunicipalityRepository, MunicipalityModelOut,
                                                             MunicipalityModelIn)
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (MunicipalityEntity)


class MunicipalityRepositoryAdapter(MunicipalityRepository):

    @staticmethod
    async def add_municipality(municipality: MunicipalityModelIn) -> MunicipalityModelOut:
        new_municipality = MunicipalityEntity(name_municipality=municipality.name_municipality,
                                              code_municipality=municipality.code_municipality,
                                              department_id=municipality.department_id)
        session.add(new_municipality)
        try:
            session.commit()
            session.refresh(new_municipality)
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a municipality with the code: {municipality.code_municipality}")
        municipality_model_out = MunicipalityModelOut(
            id_municipality=new_municipality.id_municipality,
            name_municipality=new_municipality.name_municipality,
            code_municipality=new_municipality.code_municipality,
            department_id=new_municipality.department_id
        )
        return municipality_model_out

    @staticmethod
    async def get_municipality_by_id(id_municipality: int) -> MunicipalityModelOut:
        query = session.query(MunicipalityEntity).where(MunicipalityEntity.id_municipality == id_municipality).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Municipality not found")
        else:
            municipality_model_out = MunicipalityModelOut(
                id_municipality=query.id_municipality,
                name_municipality=query.name_municipality,
                code_municipality=query.code_municipality,
                department_id=query.department_id
            )
            session.commit()
            session.close()
            return municipality_model_out

    @staticmethod
    async def update_municipality(id_municipality: int, municipality: MunicipalityModelIn) -> MunicipalityModelOut:
        query = session.query(MunicipalityEntity).where(MunicipalityEntity.id_municipality == id_municipality).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Municipality not found")
        else:
            if query:
                for key, value in municipality.dict().items():
                    setattr(query, key, value)

        municipality_model_out = MunicipalityModelOut(
            id_municipality=id_municipality,
            name_municipality=municipality.name_municipality,
            code_municipality=municipality.code_municipality,
            department_id=municipality.department_id
        )
        try:
            session.commit()
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a municipality with the code: "
                                       f"{municipality.code_municipality}")
        return municipality_model_out

    @staticmethod
    async def get_all_municipalities() -> List[MunicipalityModelOut]:
        query = session.query(MunicipalityEntity).all()
        municipalities_model_out_list = [
            MunicipalityModelOut(
                id_municipality=q.id_municipality,
                name_municipality=q.name_municipality,
                code_municipality=q.code_municipality,
                department_id=q.department_id
            )
            for q in query
        ]
        session.commit()
        session.close()
        return municipalities_model_out_list

    @staticmethod
    async def delete_municipality(id_municipality: int) -> None:
        query = session.query(MunicipalityEntity).where(MunicipalityEntity.id_municipality == id_municipality).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Municipality not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None

    @staticmethod
    async def count_municipalities() -> int:
        count_municipalities = session.query(MunicipalityEntity).count()
        return count_municipalities
