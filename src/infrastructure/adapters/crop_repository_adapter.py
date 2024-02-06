from typing import List
from fastapi import HTTPException
from src.domain.repositories.crop_repository import (CropRepository, CropModelIn, CropModelOut,
                                                     MunicipalityProductionModelOut, CropModelOut2)
from src.infrastructure.adapters.data_sources.db_config import get_db_connection, psycopg2
import json

connection = get_db_connection()


class CropRepositoryAdapter(CropRepository):
    @staticmethod
    async def add_crop(crop: CropModelIn) -> CropModelOut:
        data_query = ()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM agro_web.create_crop_agroweb(%s, %s, %s, %s, %s, %s)",
                           (crop.hectares, crop.seed_time, crop.approximate_durability_date,
                            crop.approximate_weeks_crop_durability, crop.harvest_id, crop.user_id))
            data_query = cursor.fetchall()
            connection.commit()
            cursor.close()
        except psycopg2.DatabaseError as error:
            connection.rollback()
            print(error)
            raise HTTPException(status_code=400,
                                detail=f"Error: {error}")
        print(data_query)
        if data_query[0][0] is False:
            raise HTTPException(status_code=400,
                                detail=f"Transaction error in DB: '{data_query[0][1]}'")
        response_json = json.loads(data_query[0][2])
        return CropModelOut(
            hectares=crop.hectares,
            seed_time=crop.seed_time,
            approximate_durability_date=crop.approximate_durability_date,
            approximate_weeks_crop_durability=crop.approximate_weeks_crop_durability,
            harvest_id=crop.harvest_id,
            user_id=crop.user_id,
            id_crop=response_json["id_crop"],
            activate=response_json["activate"]
        )
        # new_crop = CropEntity(hectares=crop.hectares, seed_time=crop.seed_time,
        #                       approximate_durability_date=crop.approximate_durability_date,
        #                       approximate_weeks_crop_durability=crop.approximate_weeks_crop_durability,
        #                       harvest_id=crop.harvest_id, user_id=crop.user_id, activate=True)
        # session.add(new_crop)
        # session.commit()
        # session.refresh(new_crop)
        # session.close()
        # crop_model_out = CropModelOut(
        #     id_crop=new_crop.id_crop,
        #     hectares=new_crop.hectares,
        #     seed_time=new_crop.seed_time,
        #     approximate_durability_date=new_crop.approximate_durability_date,
        #     approximate_weeks_crop_durability=new_crop.approximate_weeks_crop_durability,
        #     activate=new_crop.activate,
        #     harvest_id=new_crop.harvest_id,
        #     user_id=new_crop.user_id
        # )
        # return crop_model_out
        pass

    @staticmethod
    async def get_crop_by_id(id_crop: int) -> CropModelOut2:
        # query = (
        #     session.query(CropEntity, HarvestEntity)
        #     .join(HarvestEntity, CropEntity.harvest_id == HarvestEntity.id_harvest)
        #     .where(CropEntity.id_crop == id_crop).first()
        # )
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Crop not found")
        # else:
        #     crop_model_out = CropModelOut2(
        #         id_crop=query.CropEntity.id_crop,
        #         hectares=query.CropEntity.hectares,
        #         seed_time=query.CropEntity.seed_time,
        #         approximate_durability_date=query.CropEntity.approximate_durability_date,
        #         approximate_weeks_crop_durability=query.CropEntity.approximate_weeks_crop_durability,
        #         activate=query.CropEntity.activate,
        #         harvest_id=query.CropEntity.harvest_id,
        #         user_id=query.CropEntity.user_id,
        #         name_harvest=query.HarvestEntity.name_harvest,
        #         code_harvest=query.HarvestEntity.code_harvest,
        #         id_harvest=query.HarvestEntity.id_harvest
        #     )
        #     session.commit()
        #     session.close()
        #     return crop_model_out
        pass

    @staticmethod
    async def update_crop(id_crop: int, crop: CropModelIn) -> CropModelOut:
        # query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Crop not found")
        # else:
        #     if query:
        #         for key, value in crop.dict().items():
        #             setattr(query, key, value)
        #
        # crop_model_out = CropModelOut(
        #     id_crop=id_crop,
        #     hectares=crop.hectares,
        #     seed_time=crop.seed_time,
        #     approximate_durability_date=crop.approximate_durability_date,
        #     approximate_weeks_crop_durability=crop.approximate_weeks_crop_durability,
        #     activate=query.activate,
        #     harvest_id=crop.harvest_id,
        #     user_id=crop.user_id
        # )
        # session.commit()
        # session.close()
        # return crop_model_out
        pass

    @staticmethod
    async def get_all_crops(user_id: int, user_login: int) -> List[CropModelOut2]:
        data_query = ()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM agro_web.get_all_crops_by_user(%s, %s)", (user_id, user_login))
            data_query = cursor.fetchall()
            connection.commit()
            cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)
            connection.rollback()
            raise HTTPException(status_code=400,
                                detail=f"Error: {error}")
        if data_query[0][0] is False:
            raise HTTPException(status_code=400,
                                detail=f"Transaction error in DB: '{data_query[0][1]}'")
        if data_query[0][2] is not None:
            response_json = json.loads(data_query[0][2])
            return [
                CropModelOut2(
                    hectares=item.get("hectares"),
                    seed_time=item.get("seed_time"),
                    approximate_durability_date=item.get("approximate_durability_date"),
                    approximate_weeks_crop_durability=item.get("approximate_weeks_crop_durability"),
                    harvest_id=item.get("harvest_id"),
                    user_id=item.get("user_id"),
                    id_crop=item.get("id_crop"),
                    activate=item.get("activate"),
                    name_harvest=item.get("name_harvest"),
                    code_harvest=item.get("code_harvest")
                )
                for item in response_json
            ]
        else:
            return []
        # query = (
        #     session.query(CropEntity, HarvestEntity)
        #     .join(HarvestEntity, HarvestEntity.id_harvest == CropEntity.harvest_id)
        #     .where(CropEntity.user_id == user_id).all()
        # )
        # crops_model_out_list = [
        #     CropModelOut2(
        #         id_crop=q.id_crop,
        #         hectares=q.hectares,
        #         seed_time=q.seed_time,
        #         approximate_durability_date=q.approximate_durability_date,
        #         approximate_weeks_crop_durability=q.approximate_weeks_crop_durability,
        #         activate=q.activate,
        #         harvest_id=q.harvest_id,
        #         user_id=q.user_id,
        #         name_harvest=h.name_harvest,
        #         code_harvest=h.code_harvest,
        #         id_harvest=h.id_harvest
        #     )
        #     for q, h in query
        # ]
        # session.commit()
        # session.close()
        # return crops_model_out_list
        pass

    @staticmethod
    async def delete_crop(id_crop: int) -> None:
        # query = session.query(CropEntity).where(CropEntity.id_crop == id_crop).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Crop not found")
        # else:
        #     if query:
        #         session.delete(query)
        #     session.commit()
        #     session.close()
        # return None
        pass

    @staticmethod
    async def get_all_crops_harvest_by_id(harvest_id: int) -> List[CropModelOut]:
        # query = session.query(CropEntity).where(CropEntity.harvest_id == harvest_id, CropEntity.activate).all()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        # else:
        #     crops_model_out_list = [
        #         CropModelOut(
        #             id_crop=q.id_crop,
        #             hectares=q.hectares,
        #             seed_time=q.seed_time,
        #             approximate_durability_date=q.approximate_durability_date,
        #             approximate_weeks_crop_durability=q.approximate_weeks_crop_durability,
        #             activate=q.activate,
        #             harvest_id=q.harvest_id,
        #             user_id=q.user_id
        #         )
        #         for q in query
        #     ]
        #     session.commit()
        #     session.close()
        #     return crops_model_out_list
        pass

    @staticmethod
    async def get_all_crops_past() -> List[MunicipalityProductionModelOut]:
        # query = (
        #     session.query(CropEntity, UserEntity, MunicipalityEntity, HarvestEntity)
        #     .join(UserEntity, CropEntity.user_id == UserEntity.id_user)
        #     .join(MunicipalityEntity, UserEntity.municipality_id == MunicipalityEntity.id_municipality)
        #     .join(HarvestEntity, CropEntity.harvest_id == HarvestEntity.id_harvest)
        #     .filter(CropEntity.activate)
        #     .all()
        # )
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        # else:
        #     result = [
        #         MunicipalityProductionModelOut(
        #             name_municipality=MunicipalityEntity.name_municipality,
        #             municipality_id=MunicipalityEntity.id_municipality,
        #             code_municipality=MunicipalityEntity.code_municipality,
        #             harvest_id=HarvestEntity.id_harvest,
        #             code_harvest=HarvestEntity.code_harvest,
        #             name_harvest=HarvestEntity.name_harvest,
        #             total_hectares=CropEntity.hectares
        #         )
        #         for CropEntity, UserEntity, MunicipalityEntity, HarvestEntity in query
        #     ]
        #     session.commit()
        #     session.close()
        #     return result
        pass

    @staticmethod
    async def get_most_widely_planted_crops() -> List[CropModelOut2]:
        # query = (
        #     session.query(CropEntity, HarvestEntity)
        #     .join(HarvestEntity, CropEntity.harvest_id == HarvestEntity.id_harvest)
        #     .filter(CropEntity.activate)
        #     .all()
        # )
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found or empty Crops")
        # else:
        #     result = [
        #         CropModelOut2(
        #             id_crop=CropEntity.id_crop,
        #             hectares=CropEntity.hectares,
        #             seed_time=CropEntity.seed_time,
        #             approximate_durability_date=CropEntity.approximate_durability_date,
        #             approximate_weeks_crop_durability=CropEntity.approximate_weeks_crop_durability,
        #             activate=CropEntity.activate,
        #             harvest_id=CropEntity.harvest_id,
        #             user_id=CropEntity.user_id,
        #             name_harvest=HarvestEntity.name_harvest,
        #             code_harvest=HarvestEntity.code_harvest,
        #             id_harvest=HarvestEntity.id_harvest
        #         )
        #         for CropEntity, HarvestEntity in query
        #     ]
        #     session.commit()
        #     session.close()
        #     return result
        pass

    @staticmethod
    async def count_hectares() -> int:
        # count_hectares = session.query(func.sum(CropEntity.hectares)).scalar()
        # return count_hectares
        pass
