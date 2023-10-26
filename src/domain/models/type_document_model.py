from pydantic import BaseModel
from typing import Optional


class TypeDocumentModelIn(BaseModel):
    name_type_document: str
    code_type_document: str


class TypeDocumentModelOut(TypeDocumentModelIn):
    id_type_document: int


class TypeDocumentModelUpdate(TypeDocumentModelIn):
    name_type_document: Optional[str] = None
    code_type_document: Optional[str] = None
