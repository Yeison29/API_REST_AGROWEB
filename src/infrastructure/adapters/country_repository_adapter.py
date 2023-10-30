from typing import List
from fastapi import HTTPException
from src.domain.models.country_model import CountryModelIn, CountryModelOut
from src.domain.repositories.country_repository import CountryRepository
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (CountryEntity)


class CountryRepositoryAdapter(CountryRepository):

    @staticmethod
    async def add_country(country: CountryModelIn) -> CountryModelOut:
        new_country = CountryEntity(name_country=country.name_country, code_country=country.code_country)
        session.add(new_country)
        session.commit()
        session.refresh(new_country)
        session.close()
        country_model_out = CountryModelOut(
            id_country=new_country.id_country,
            name_country=new_country.name_country,
            code_country=new_country.code_country
        )
        return country_model_out

    @staticmethod
    async def get_country_by_id(id_country: int) -> CountryModelOut:
        query = session.query(CountryEntity).where(CountryEntity.id_country == id_country).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Country not found")
        else:
            country_model_out = CountryModelOut(
                id_country=query.id_country,
                name_country=query.name_country,
                code_country=query.code_country
            )
            session.commit()
            session.close()
            return country_model_out

    @staticmethod
    async def update_country(id_country: int, country: CountryModelIn) -> CountryModelOut:
        query = session.query(CountryEntity).where(CountryEntity.id_country == id_country).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Country not found")
        else:
            if query:
                for key, value in country.dict().items():
                    setattr(query, key, value)

        country_model_out = CountryModelOut(
            id_country=id_country,
            name_country=country.name_country,
            code_country=country.code_country
        )
        session.commit()
        session.close()
        return country_model_out

    @staticmethod
    async def get_all_countries() -> List[CountryModelOut]:
        query = session.query(CountryEntity).all()
        countries_model_out_list = [
            CountryModelOut(
                id_country=q.id_country,
                name_country=q.name_country,
                code_country=q.code_country
            )
            for q in query
        ]
        session.commit()
        session.close()
        return countries_model_out_list

    @staticmethod
    async def delete_country(id_country: int) -> None:
        query = session.query(CountryEntity).where(CountryEntity.id_country == id_country).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Country not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None
