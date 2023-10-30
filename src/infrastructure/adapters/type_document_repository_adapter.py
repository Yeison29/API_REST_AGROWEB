from typing import List
from fastapi import HTTPException
from src.domain.models.type_document_model import TypeDocumentModelOut, TypeDocumentModelIn
from src.domain.repositories.type_document_repository import TypeDocumentRepository
from src.infrastructure.adapters.data_sources.db_config import session
from src.infrastructure.adapters.data_sources.entities.agro_web_entity import (TypeDocumentEntity)


class TypeDocumentRepositoryAdapter(TypeDocumentRepository):

    @staticmethod
    async def add_type_document(type_document: TypeDocumentModelIn) -> TypeDocumentModelOut:
        new_type_document = TypeDocumentEntity(name_type_document=type_document.name_type_document, code_type_document=type_document.code_type_document)
        session.add(new_type_document)
        session.commit()
        session.refresh(new_type_document)
        session.close()
        type_document_model_out = TypeDocumentModelOut(
            id_type_document=new_type_document.id_type_document,
            name_type_docuemnt=new_type_document.name_type_document,
            code_type_document=new_type_document.code_type_document
        )
        return type_document_model_out

    @staticmethod
    async def get_type_document_by_id(id_type_document: int) -> TypeDocumentModelOut:
        query = session.query(TypeDocumentEntity).where(TypeDocumentEntity.id_type_document == id_type_document).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Type Document not found")
        else:
            type_document_model_out = TypeDocumentModelOut(
                id_type_document=query.id_type_document,
                name_type_document=query.name_type_document,
                code_type_document=query.code_type_docuemnt
            )
            session.commit()
            session.close()
            return type_document_model_out

    @staticmethod
    async def update_type_document(id_type_document: int, type_document: TypeDocumentModelIn) -> TypeDocumentModelOut:
        query = session.query(TypeDocumentEntity).where(TypeDocumentEntity.id_type_document == id_type_document).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Type Document not found")
        else:
            if query:
                for key, value in type_document.dict().items():
                    setattr(query, key, value)

        type_document_model_out = TypeDocumentModelOut(
            id_type_document=id_type_document,
            name_type_document=type_document.name_type_document,
            code_gender=type_document.code_type_document
        )
        session.commit()
        session.close()
        return type_document_model_out

    @staticmethod
    async def get_all_type_documents() -> List[TypeDocumentModelOut]:
        query = session.query(TypeDocumentEntity).all()
        type_documents_model_out_list = [
            TypeDocumentModelOut(
                id_type_document=q.id_type_document,
                name_type_document=q.name_type_document,
                code_type_document=q.code_type_document
            )
            for q in query
        ]
        session.commit()
        session.close()
        return type_documents_model_out_list

    @staticmethod
    async def delete_type_document(id_type_document: int) -> None:
        query = session.query(TypeDocumentEntity).where(TypeDocumentEntity.id_type_document == id_type_document).first()
        if not query:
            session.commit()
            session.close()
            raise HTTPException(status_code=404, detail="Type Document not found")
        else:
            if query:
                session.delete(query)
            session.commit()
            session.close()
        return None