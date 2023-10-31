from typing import List
from src.infrastructure.adapters.type_document_repository_adapter import (TypeDocumentRepositoryAdapter,
                                                                          TypeDocumentModelOut, TypeDocumentModelIn)
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase

type_document_repository = TypeDocumentRepositoryAdapter


class TypeDocumentUseCase:

    @staticmethod
    async def add_type_document(type_document: TypeDocumentModelIn, token: str) -> TypeDocumentModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            response = await type_document_repository.add_type_document(type_document)
            return response

    @staticmethod
    async def get_type_document_by_id(id_type_document: int, token: str) -> TypeDocumentModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            type_document = await type_document_repository.get_type_document_by_id(id_type_document)
            return type_document

    @staticmethod
    async def update_type_document(id_type_document: int, type_document_update: TypeDocumentModelIn,  token: str
                                   ) -> TypeDocumentModelOut:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            updated_type_document = await type_document_repository.update_type_document(id_type_document,
                                                                                        type_document_update)
            return updated_type_document

    @staticmethod
    async def get_all_type_documents() -> List[TypeDocumentModelOut]:
        type_documents = await type_document_repository.get_all_type_documents()
        return type_documents

    @staticmethod
    async def delete_type_document(id_type_document: int, token: str) -> None:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            delete_type_document = await type_document_repository.delete_type_document(id_type_document)
            return delete_type_document
