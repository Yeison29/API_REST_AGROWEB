from typing import List
from fastapi import HTTPException
from src.domain.repositories.crop_repository import CropRepository, CropModelIn, CropModelOut
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (CropEntity)


class CropRepositoryAdapter(CropRepository):
    @staticmethod
    async def add_crop(crop: CropModelIn) -> CropModelOut:
        new_crop = CropEntity(hectares=crop.hectares, seed_time=crop.seed_time,
                              approximate_durability_date=crop.approximate_durability_date,
                              approximate_weeks_crop_durability=crop.approximate_weeks_crop_durability,
                              harvest_id=crop.harvest_id, user_id=crop.user_id, activate=True)
        session.add(new_crop)
        session.commit()
        session.refresh(new_crop)
        session.close()
        crop_model_out = CropModelOut(
            id_crop=new_crop.id_crop,
            hectares=new_crop.hectares,
            seed_time=new_crop.seed_time,
            approximate_durability_date=new_crop.approximate_durability_date,
            approximate_weeks_crop_durability=new_crop.approximate_weeks_crop_durability,
            activate=new_crop.activate,
            harvest_id=new_crop.harvest_id,
            user_id=new_crop.user_id
        )
        return crop_model_out

    @staticmethod
    async def get_crop_by_id(id_crop: int) -> CropModelOut:
        query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Crop not found")
        else:
            crop_model_out = CropModelOut(
                id_crop=query.id_crop,
                hectares=query.hectares,
                seed_time=query.seed_time,
                approximate_durability_date=query.approximate_durability_date,
                approximate_weeks_crop_durability=query.approximate_weeks_crop_durability,
                activate=query.activate,
                harvest_id=query.harvest_id,
                user_id=query.user_id
            )
            session.commit()
            session.close()
            return crop_model_out

    @staticmethod
    async def update_crop(id_crop: int, crop: CropModelIn) -> CropModelOut:
        query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Crop not found")
        else:
            if query:
                for key, value in crop.dict().items():
                    setattr(query, key, value)

        crop_model_out = CropModelOut(
            id_crop=id_crop,
            hectares=crop.hectares,
            seed_time=crop.seed_time,
            approximate_durability_date=crop.approximate_durability_date,
            approximate_weeks_crop_durability=crop.approximate_weeks_crop_durability,
            activate=query.activate,
            harvest_id=crop.harvest_id,
            user_id=crop.user_id
        )
        session.commit()
        session.close()
        return crop_model_out

    @staticmethod
    async def get_all_crops() -> List[CropModelOut]:
        query = session.query(CropEntity).all()
        crops_model_out_list = [
            CropModelOut(
                id_crop=q.id_crop,
                hectares=q.hectares,
                seed_time=q.seed_time,
                approximate_durability_date=q.approximate_durability_date,
                approximate_weeks_crop_durability=q.approximate_weeks_crop_durability,
                activate=q.activate,
                harvest_id=q.harvest_id,
                user_id=q.user_id
            )
            for q in query
        ]
        session.commit()
        session.close()
        return crops_model_out_list

    @staticmethod
    async def delete_crop(id_crop: int) -> None:
        query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Crop not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None

    @staticmethod
    async def gat_all_crops_harvest_by_id(harvest_id: int) -> List[CropModelOut]:
        query = session.query(CropEntity).where(CropEntity.harvest_id == harvest_id, CropEntity.activate).all()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        else:
            crops_model_out_list = [
                CropModelOut(
                    id_crop=q.id_crop,
                    hectares=q.hectares,
                    seed_time=q.seed_time,
                    approximate_durability_date=q.approximate_durability_date,
                    approximate_weeks_crop_durability=q.approximate_weeks_crop_durability,
                    activate=q.activate,
                    harvest_id=q.harvest_id,
                    user_id=q.user_id
                )
                for q in query
            ]
            session.commit()
            session.close()
            return crops_model_out_list