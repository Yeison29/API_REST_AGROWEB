from typing import List
from fastapi import HTTPException
from src.domain.repositories.crop_repository import (CropRepository, CropModelIn, CropModelOut,
                                                     MunicipalityProductionModelOut, CropModelOut2)
from src.infrastructure.adapters.data_sources.db_config import session, func
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (CropEntity, UserEntity,
                                                                               MunicipalityEntity, HarvestEntity)


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
    async def get_crop_by_id(id_crop: int) -> CropModelOut2:
        query = (
            session.query(CropEntity, HarvestEntity)
            .join(HarvestEntity, CropEntity.harvest_id == HarvestEntity.id_harvest)
            .where(CropEntity.id_crop == id_crop).first()
        )
        if not query:
            session.commit()
            raise HTTPException(status_code=404, detail="Crop not found")
        else:
            crop_model_out = CropModelOut2(
                id_crop=query.CropEntity.id_crop,
                hectares=query.CropEntity.hectares,
                seed_time=query.CropEntity.seed_time,
                approximate_durability_date=query.CropEntity.approximate_durability_date,
                approximate_weeks_crop_durability=query.CropEntity.approximate_weeks_crop_durability,
                activate=query.CropEntity.activate,
                harvest_id=query.CropEntity.harvest_id,
                user_id=query.CropEntity.user_id,
                name_harvest=query.HarvestEntity.name_harvest,
                code_harvest=query.HarvestEntity.code_harvest,
                id_harvest=query.HarvestEntity.id_harvest
            )
            session.commit()
            return crop_model_out

    @staticmethod
    async def update_crop(id_crop: int, crop: CropModelIn) -> CropModelOut:
        query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        if not query:
            session.commit()
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
        return crop_model_out

    @staticmethod
    async def get_all_crops(user_id: int) -> List[CropModelOut2]:
        query = (
            session.query(CropEntity, HarvestEntity)
            .join(HarvestEntity, HarvestEntity.id_harvest == CropEntity.harvest_id)
            .where(CropEntity.user_id == user_id).all()
        )
        crops_model_out_list = CropRepositoryAdapter.crops_model_out_list(query)
        session.commit()
        return crops_model_out_list

    @staticmethod
    async def delete_crop(id_crop: int) -> None:
        query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        if not query:
            session.commit()
            
            raise HTTPException(status_code=404, detail="Crop not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            
        return None

    @staticmethod
    async def get_all_crops_harvest_by_id(harvest_id: int) -> List[CropModelOut]:
        query = session.query(CropEntity).where(CropEntity.harvest_id == harvest_id, CropEntity.activate).all()
        if not query:
            session.commit()
            
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
            
            return crops_model_out_list

    @staticmethod
    async def get_all_crops_past() -> List[MunicipalityProductionModelOut]:
        query = (
            session.query(CropEntity, MunicipalityEntity, HarvestEntity)
            .join(UserEntity, CropEntity.user_id == UserEntity.id_user)
            .join(MunicipalityEntity, UserEntity.municipality_id == MunicipalityEntity.id_municipality)
            .join(HarvestEntity, CropEntity.harvest_id == HarvestEntity.id_harvest)
            .filter(CropEntity.activate)
            .all()
        )
        if not query:
            session.commit()
            
            raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        else:
            result = [
                MunicipalityProductionModelOut(
                    name_municipality=municipality_entity.name_municipality,
                    municipality_id=municipality_entity.id_municipality,
                    code_municipality=municipality_entity.code_municipality,
                    harvest_id=harvest_entity.id_harvest,
                    code_harvest=harvest_entity.code_harvest,
                    name_harvest=harvest_entity.name_harvest,
                    total_hectares=crop_entity.hectares
                )
                for crop_entity, municipality_entity, harvest_entity in query
            ]
            session.commit()
            return result

    @staticmethod
    async def get_most_widely_planted_crops() -> List[CropModelOut2]:
        query = (
            session.query(CropEntity, HarvestEntity)
            .join(HarvestEntity, CropEntity.harvest_id == HarvestEntity.id_harvest)
            .filter(CropEntity.activate)
            .all()
        )
        if not query:
            session.commit()
            
            raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        else:
            result = CropRepositoryAdapter.crops_model_out_list(query)
            session.commit()
            return result
        pass

    @staticmethod
    async def count_hectares() -> int:
        count_hectares = session.query(func.sum(CropEntity.hectares)).scalar()
        return count_hectares

    @staticmethod
    def crops_model_out_list(query: any) -> List[CropModelOut2]:
        return [
                CropModelOut2(
                    id_crop=crop_entity.id_crop,
                    hectares=crop_entity.hectares,
                    seed_time=crop_entity.seed_time,
                    approximate_durability_date=crop_entity.approximate_durability_date,
                    approximate_weeks_crop_durability=crop_entity.approximate_weeks_crop_durability,
                    activate=crop_entity.activate,
                    harvest_id=crop_entity.harvest_id,
                    user_id=crop_entity.user_id,
                    name_harvest=harvest_entity.name_harvest,
                    code_harvest=harvest_entity.code_harvest,
                    id_harvest=harvest_entity.id_harvest
                )
                for crop_entity, harvest_entity in query
            ]
