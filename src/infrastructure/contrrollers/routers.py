from typing import List
from src.domain.models.gender_model import GenderModelOut
from src.domain.models.user_model import UserModelOut
from src.domain.models.token_model import TokenModel
from fastapi import APIRouter
from src.infrastructure.contrrollers.api_rest import ApiRest


class ApiRouter:

    def __init__(self):
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        self.router.post("/token", status_code=200, response_model=TokenModel)(ApiRest.token)
        self.router.get("/get-all-users", status_code=200, response_model=List[UserModelOut])(ApiRest.get_all_users)
        self.router.post("/api/create-user", status_code=201, response_model=UserModelOut)(ApiRest.add_user)
        self.router.get("/api/get-user-by-id", status_code=200, response_model=UserModelOut)(ApiRest.get_user_by_id)
        self.router.put("/api/update-user", status_code=201, response_model=UserModelOut)(ApiRest.update_user)
        self.router.delete("/api/delete-user", status_code=204, response_model=None)(ApiRest.delete_user)
        self.router.post("/api/create-gender", status_code=201, response_model=GenderModelOut)(ApiRest.add_gender)
        (self.router.get("/api/get-all-gender", status_code=200, response_model=List[GenderModelOut])
         (ApiRest.get_all_genders))
