from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.domain.repositories.department_repository import DepartmentRepository, DepartmentModelOut, DepartmentModelIn
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (DepartmentEntity)


class DepartmentRepositoryAdapter(DepartmentRepository):

    @staticmethod
    async def add_department(department: DepartmentModelIn) -> DepartmentModelOut:
        new_department = DepartmentEntity(name_department=department.name_department,
                                          code_department=department.code_department, country_id=department.country_id)
        session.add(new_department)
        try:
            session.commit()
            session.refresh(new_department)
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a department with the code: {department.code_department}")
        country_model_out = DepartmentModelOut(
            id_department=new_department.id_department,
            name_department=new_department.name_department,
            code_department=new_department.code_department,
            country_id=new_department.country_id
        )
        return country_model_out

    @staticmethod
    async def get_department_by_id(id_department: int) -> DepartmentModelOut:
        query = session.query(DepartmentEntity).where(DepartmentEntity.id_department == id_department).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Department not found")
        else:
            department_model_out = DepartmentModelOut(
                id_department=query.id_department,
                name_department=query.name_department,
                code_department=query.code_department,
                country_id=query.country_id
            )
            session.commit()
            session.close()
            return department_model_out

    @staticmethod
    async def update_department(id_department: int, department: DepartmentModelIn) -> DepartmentModelOut:
        query = session.query(DepartmentEntity).where(DepartmentEntity.id_department == id_department).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Department not found")
        else:
            if query:
                for key, value in department.dict().items():
                    setattr(query, key, value)

        department_model_out = DepartmentModelOut(
            id_department=id_department,
            name_department=department.name_department,
            code_department=department.code_department,
            country_id=department.country_id
        )
        try:
            session.commit()
            session.close()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail=f"There is already a department with the code: {department.code_department}")
        return department_model_out

    @staticmethod
    async def get_all_departments(id_country: int) -> List[DepartmentModelOut]:
        query = session.query(DepartmentEntity).where(DepartmentEntity.country_id == id_country).all()
        departments_model_out_list = [
            DepartmentModelOut(
                id_department=q.id_department,
                name_department=q.name_department,
                code_department=q.code_department,
                country_id=q.country_id
            )
            for q in query
        ]
        session.commit()
        session.close()
        return departments_model_out_list

    @staticmethod
    async def delete_department(id_department: int) -> None:
        query = session.query(DepartmentEntity).where(DepartmentEntity.id_department == id_department).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Department not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None
