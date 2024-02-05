from typing import List
from fastapi import HTTPException
from src.domain.repositories.municipality_repository import (MunicipalityRepository, MunicipalityModelOut,
                                                             MunicipalityModelIn)
from src.infrastructure.adapters.data_sources.db_config import get_db_connection, psycopg2
import json

connection = get_db_connection()


class MunicipalityRepositoryAdapter(MunicipalityRepository):

    @staticmethod
    async def add_municipality(municipality: MunicipalityModelIn) -> MunicipalityModelOut:
        # new_municipality = MunicipalityEntity(name_municipality=municipality.name_municipality,
        #                                       code_municipality=municipality.code_municipality,
        #                                       department_id=municipality.department_id)
        # session.add(new_municipality)
        # try:
        #     session.commit()
        #     session.refresh(new_municipality)
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a municipality with the code: {municipality.code_municipality}")
        # municipality_model_out = MunicipalityModelOut(
        #     id_municipality=new_municipality.id_municipality,
        #     name_municipality=new_municipality.name_municipality,
        #     code_municipality=new_municipality.code_municipality,
        #     department_id=new_municipality.department_id
        # )
        # return municipality_model_out
        pass

    @staticmethod
    async def get_municipality_by_id(id_municipality: int) -> MunicipalityModelOut:
        # query = session.query(MunicipalityEntity).where(MunicipalityEntity.id_municipality == id_municipality).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Municipality not found")
        # else:
        #     municipality_model_out = MunicipalityModelOut(
        #         id_municipality=query.id_municipality,
        #         name_municipality=query.name_municipality,
        #         code_municipality=query.code_municipality,
        #         department_id=query.department_id
        #     )
        #     session.commit()
        #     session.close()
        #     return municipality_model_out
        pass

    @staticmethod
    async def update_municipality(id_municipality: int, municipality: MunicipalityModelIn) -> MunicipalityModelOut:
        # query = session.query(MunicipalityEntity).where(MunicipalityEntity.id_municipality == id_municipality).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Municipality not found")
        # else:
        #     if query:
        #         for key, value in municipality.dict().items():
        #             setattr(query, key, value)
        #
        # municipality_model_out = MunicipalityModelOut(
        #     id_municipality=id_municipality,
        #     name_municipality=municipality.name_municipality,
        #     code_municipality=municipality.code_municipality,
        #     department_id=municipality.department_id
        # )
        # try:
        #     session.commit()
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a municipality with the code: "
        #                                f"{municipality.code_municipality}")
        # return municipality_model_out
        pass

    @staticmethod
    async def get_all_municipalities(id_department: int) -> List[MunicipalityModelOut]:
        data_query = ()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM agro_web.get_all_municipalities_by_department(%s)",
                (id_department,)
            )
            data_query = cursor.fetchall()
            connection.commit()
            cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)
            connection.rollback()
            raise HTTPException(status_code=400,
                                detail=f"Error: {error}")
        print(data_query)
        if data_query[0][0] is False:
            raise HTTPException(status_code=400,
                                detail=f"Transaction error in DB: '{data_query[0][1]}'")
        if data_query[0][2] is not None:
            response_json = json.loads(data_query[0][2])
            return [
                MunicipalityModelOut(
                    name_municipality=item.get('name_municipality', ''),
                    department_id=id_department,
                    id_municipality=item.get('id_municipality', '')
                )
                for item in response_json
            ]
        else:
            return []

        # query = session.query(MunicipalityEntity).where(MunicipalityEntity.department_id == id_department).all()
        # municipalities_model_out_list = [
        #     MunicipalityModelOut(
        #         id_municipality=q.id_municipality,
        #         name_municipality=q.name_municipality,
        #         code_municipality=q.code_municipality,
        #         department_id=q.department_id
        #     )
        #     for q in query
        # ]
        # session.commit()
        # session.close()
        # return municipalities_model_out_list
        pass

    @staticmethod
    async def delete_municipality(id_municipality: int) -> None:
        # query = session.query(MunicipalityEntity).where(MunicipalityEntity.id_municipality == id_municipality).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Municipality not found")
        # else:
        #     if query:
        #         session.delete(query)
        #     session.commit()
        #     session.close()
        # return None
        pass

    @staticmethod
    async def count_municipalities() -> int:
        # count_municipalities = session.query(MunicipalityEntity).count()
        # return count_municipalities
        pass
