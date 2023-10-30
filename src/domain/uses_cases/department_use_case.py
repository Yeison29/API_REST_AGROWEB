from typing import List
from src.domain.models.department_model import DepartmentModelOut, DepartmentModelIn
from src.infrastructure.adapters.department_repository_adapter import DepartmentRepositoryAdapter
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

department_repository = DepartmentRepositoryAdapter


class DepartmentUseCase:

    @staticmethod
    async def add_department(department: DepartmentModelIn, token: str) -> DepartmentModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await department_repository.add_department(department)
            return response

    @staticmethod
    async def get_department_by_id(id_department: int, token: str) -> DepartmentModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            department = await department_repository.get_department_by_id(id_department)
            return department

    @staticmethod
    async def update_department(id_department: int, department_update: DepartmentModelIn,  token: str) -> (
            DepartmentModelOut):
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_department = await department_repository.update_department(id_department, department_update)
            return updated_department

    @staticmethod
    async def get_all_departments() -> List[DepartmentModelOut]:
        departments = await department_repository.get_all_departments()
        return departments

    @staticmethod
    async def delete_department(id_department: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_department = await department_repository.delete_department(id_department)
            return delete_department
    