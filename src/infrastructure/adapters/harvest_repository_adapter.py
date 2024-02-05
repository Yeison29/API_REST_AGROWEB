from typing import List
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from src.domain.repositories.harvest_repository import HarvestRepository, HarvestModelIn, HarvestModelOut
from src.infrastructure.adapters.data_sources.db_config import get_db_connection, psycopg2
import json

connection = get_db_connection()


class HarvestRepositoryAdapter(HarvestRepository):

    @staticmethod
    async def add_harvest(harvest: HarvestModelIn) -> HarvestModelOut:
        # new_harvest = HarvestEntity(name_harvest=harvest.name_harvest, code_harvest=harvest.code_harvest)
        # session.add(new_harvest)
        # try:
        #     session.commit()
        #     session.refresh(new_harvest)
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a harvest with the code: {harvest.code_harvest}")
        # harvest_model_out = HarvestModelOut(
        #     id_harvest=new_harvest.id_harvest,
        #     name_harvest=new_harvest.name_harvest,
        #     code_harvest=new_harvest.code_harvest
        # )
        # return harvest_model_out
        pass

    @staticmethod
    async def get_harvest_by_id(id_harvest: int) -> HarvestModelOut:
        # query = session.query(HarvestEntity).where(HarvestEntity.id_harvest == id_harvest).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found")
        # else:
        #     harvest_model_out = HarvestModelOut(
        #         id_harvest=query.id_harvest,
        #         name_harvest=query.name_harvest,
        #         code_harvest=query.code_harvest
        #     )
        #     session.commit()
        #     session.close()
        #     return harvest_model_out
        pass

    @staticmethod
    async def update_harvest(id_harvest: int, harvest: HarvestModelIn) -> HarvestModelOut:
        # query = session.query(HarvestEntity).where(HarvestEntity.id_harvest == id_harvest).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found")
        # else:
        #     if query:
        #         for key, value in harvest.dict().items():
        #             setattr(query, key, value)
        #
        # harvest_model_out = HarvestModelOut(
        #     id_harvest=id_harvest,
        #     name_harvest=harvest.name_harvest,
        #     code_harvest=harvest.code_harvest
        # )
        # try:
        #     session.commit()
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a harvest with the code: {harvest.code_harvest}")
        # return harvest_model_out
        pass

    @staticmethod
    async def get_all_harvests() -> List[HarvestModelOut]:
        data_query = ()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM agro_web.get_all_harvests()")
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
                HarvestModelOut(
                    name_harvest=item.get("name_harvest"),
                    code_harvest=item.get("code_harvest"),
                    id_harvest=item.get("id_harvest")
                )
                for item in response_json
            ]
        else:
            return []
        # query = session.query(HarvestEntity).all()
        # harvests_model_out_list = [
        #     HarvestModelOut(
        #         id_harvest=q.id_harvest,
        #         name_harvest=q.name_harvest,
        #         code_harvest=q.code_harvest
        #     )
        #     for q in query
        # ]
        # session.commit()
        # session.close()
        # return harvests_model_out_list
        pass

    @staticmethod
    async def delete_harvest(id_harvest: int) -> None:
        # query = session.query(HarvestEntity).where(HarvestEntity.id_harvest == id_harvest).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Harvest not found")
        # else:
        #     if query:
        #         session.delete(query)
        #     session.commit()
        #     session.close()
        # return None
        pass

    @staticmethod
    async def count_harvests() -> int:
        # count_harvests = session.query(HarvestEntity).count()
        # return count_harvests
        pass
