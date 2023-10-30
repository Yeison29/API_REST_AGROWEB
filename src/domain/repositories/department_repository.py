from typing import List
from abc import ABC, abstractmethod
from src.domain.models.department_model import DepartmentModelOut, DepartmentModelIn


class DepartmentRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_department(department: DepartmentModelIn) -> DepartmentModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_department_by_id(id_department: int) -> DepartmentModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_department(id_department: int, department: DepartmentModelIn) -> DepartmentModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_departments() -> List[DepartmentModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_department(id_department: int) -> None:
        pass
