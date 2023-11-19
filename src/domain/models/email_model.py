from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any


class EmailModel(BaseModel):
    email: List[EmailStr]
    body: Dict[str, Any]
