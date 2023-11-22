from typing import List
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from src.domain.repositories.harvest_repository import HarvestRepository, HarvestModelIn, HarvestModelOut
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (HarvestEntity)


class HarvestRepositoryAdapter(HarvestRepository):

    @staticmethod
    async def add_harvest(harvest: HarvestModelIn) -> HarvestModelOut:
        new_harvest = HarvestEntity(name_harvest=harvest.name_harvest, code_harvest=harvest.code_harvest)
        session.add(new_harvest)
        try:
            session.commit()
            session.refresh(new_harvest)
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a harvest with the code: {harvest.code_harvest}")
        harvest_model_out = HarvestModelOut(
            id_harvest=new_harvest.id_harvest,
            name_harvest=new_harvest.name_harvest,
            code_harvest=new_harvest.code_harvest
        )
        return harvest_model_out

    @staticmethod
    async def get_harvest_by_id(id_harvest: int) -> HarvestModelOut:
        query = session.query(HarvestEntity).where(HarvestEntity.id_harvest == id_harvest).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Harvest not found")
        else:
            harvest_model_out = HarvestModelOut(
                id_harvest=query.id_harvest,
                name_harvest=query.name_harvest,
                code_harvest=query.code_harvest
            )
            session.commit()
            session.close()
            return harvest_model_out

    @staticmethod
    async def update_harvest(id_harvest: int, harvest: HarvestModelIn) -> HarvestModelOut:
        query = session.query(HarvestEntity).where(HarvestEntity.id_harvest == id_harvest).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Harvest not found")
        else:
            if query:
                for key, value in harvest.dict().items():
                    setattr(query, key, value)

        harvest_model_out = HarvestModelOut(
            id_harvest=id_harvest,
            name_harvest=harvest.name_harvest,
            code_harvest=harvest.code_harvest
        )
        try:
            session.commit()
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a harvest with the code: {harvest.code_harvest}")
        return harvest_model_out

    @staticmethod
    async def get_all_harvests() -> List[HarvestModelOut]:
        query = session.query(HarvestEntity).all()
        harvests_model_out_list = [
            HarvestModelOut(
                id_harvest=q.id_harvest,
                name_harvest=q.name_harvest,
                code_harvest=q.code_harvest
            )
            for q in query
        ]
        session.commit()
        session.close()
        return harvests_model_out_list

    @staticmethod
    async def delete_harvest(id_harvest: int) -> None:
        query = session.query(HarvestEntity).where(HarvestEntity.id_harvest == id_harvest).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Harvest not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None

    @staticmethod
    async def count_harvests() -> int:
        count_harvests = session.query(HarvestEntity).count()
        return count_harvests
