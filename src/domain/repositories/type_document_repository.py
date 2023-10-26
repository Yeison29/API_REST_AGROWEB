from typing import List
from abc import ABC, abstractmethod
from src.domain.models.type_document_model import TypeDocumentModelIn, TypeDocumentModelOut


class TypeDocumentRepository(ABC):

    @staticmethod
    @abstractmethod
    async def add_type_document(type_document: TypeDocumentModelIn) -> TypeDocumentModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_type_document_by_id(id_type_document: int) -> TypeDocumentModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def update_type_document(id_type_document: int, type_document: TypeDocumentModelIn) -> TypeDocumentModelOut:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_type_documents() -> List[TypeDocumentModelOut]:
        pass

    @staticmethod
    @abstractmethod
    async def delete_type_document(id_type_document: int) -> None:
        pass
