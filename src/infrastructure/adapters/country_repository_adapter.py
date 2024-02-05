from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.domain.repositories.country_repository import CountryRepository, CountryModelIn, CountryModelOut
from src.infrastructure.adapters.data_sources.db_config import get_db_connection, psycopg2
import json

connection = get_db_connection()

class CountryRepositoryAdapter(CountryRepository):

    @staticmethod
    async def add_country(country: CountryModelIn) -> CountryModelOut:
        # new_country = CountryEntity(name_country=country.name_country, code_country=country.code_country)
        # session.add(new_country)
        # try:
        #     session.commit()
        #     session.refresh(new_country)
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a country with the code: {country.code_country}")
        # country_model_out = CountryModelOut(
        #     id_country=new_country.id_country,
        #     name_country=new_country.name_country,
        #     code_country=new_country.code_country
        # )
        # return country_model_out
        pass

    @staticmethod
    async def get_country_by_id(id_country: int) -> CountryModelOut:
        # query = session.query(CountryEntity).where(CountryEntity.id_country == id_country).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Country not found")
        # else:
        #     country_model_out = CountryModelOut(
        #         id_country=query.id_country,
        #         name_country=query.name_country,
        #         code_country=query.code_country
        #     )
        #     session.commit()
        #     session.close()
        #     return country_model_out
        pass

    @staticmethod
    async def update_country(id_country: int, country: CountryModelIn) -> CountryModelOut:
        # query = session.query(CountryEntity).where(CountryEntity.id_country == id_country).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Country not found")
        # else:
        #     if query:
        #         for key, value in country.dict().items():
        #             setattr(query, key, value)
        #
        # country_model_out = CountryModelOut(
        #     id_country=id_country,
        #     name_country=country.name_country,
        #     code_country=country.code_country
        # )
        # try:
        #     session.commit()
        #     session.close()
        # except IntegrityError:
        #     session.rollback()
        #     raise HTTPException(status_code=400,
        #                         detail=f"There is already a country with the code: {country.code_country}")
        # return country_model_out
        pass

    @staticmethod
    async def get_all_countries() -> List[CountryModelOut]:
        data_query = ()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM agro_web.get_all_countries()")
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
                CountryModelOut(
                    name_country=item.get("name_country"),
                    code_country=item.get("code_country"),
                    id_country=item.get("id_country")
                )
                for item in response_json
            ]
        else:
            return []
        # query = session.query(CountryEntity).all()
        # countries_model_out_list = [
        #     CountryModelOut(
        #         id_country=q.id_country,
        #         name_country=q.name_country,
        #         code_country=q.code_country
        #     )
        #     for q in query
        # ]
        # session.commit()
        # session.close()
        # return countries_model_out_list
        pass

    @staticmethod
    async def delete_country(id_country: int) -> None:
        # query = session.query(CountryEntity).where(CountryEntity.id_country == id_country).first()
        # if not query:
        #     session.commit()
        #     session.close()
        #     raise HTTPException(status_code=404, detail="Country not found")
        # else:
        #     if query:
        #         session.delete(query)
        #     session.commit()
        #     session.close()
        # return None
        pass
