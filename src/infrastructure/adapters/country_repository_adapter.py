from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.domain.repositories.country_repository import CountryRepository, CountryModelIn, CountryModelOut


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
