from fastapi import APIRouter
from typing import List
from src.domain.uses_cases.gender_use_cases import GenderModelOut
from src.domain.uses_cases.user_use_cases import UserModelOut
from src.domain.uses_cases.authentication_use_cases import TokenModel
from src.domain.uses_cases.type_document_use_cases import TypeDocumentModelOut
from src.domain.uses_cases.country_use_cases import CountryModelOut
from src.domain.uses_cases.department_use_cases import DepartmentModelOut
from src.domain.uses_cases.municipality_use_cases import MunicipalityModelOut
from src.domain.uses_cases.haverst_use_cases import HarvestModelOut
from src.domain.uses_cases.crop_use_cases import CropModelOut
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
        self.router.put("/api/update-user", status_code=200, response_model=UserModelOut)(ApiRest.update_user)
        self.router.delete("/api/delete-user", status_code=204, response_model=None)(ApiRest.delete_user)
        self.router.post("/api/create-gender", status_code=201, response_model=GenderModelOut)(ApiRest.add_gender)
        self.router.get("/api/get-all-gender", status_code=200, response_model=List[GenderModelOut])(
            ApiRest.get_all_genders)
        self.router.get("/api/get-gender-by-id", status_code=200, response_model=GenderModelOut)(
            ApiRest.get_gender_by_id)
        self.router.put("/api/update-gender", status_code=200, response_model=GenderModelOut)(ApiRest.update_gender)
        self.router.delete("/api/delete-gender", status_code=204, response_model=None)(ApiRest.delete_gender)
        self.router.post("/api/create-type-document", status_code=201, response_model=TypeDocumentModelOut)(
            ApiRest.add_type_document)
        self.router.get("/api/get-all-type-documents", status_code=200, response_model=List[TypeDocumentModelOut])(
            ApiRest.get_all_type_documents)
        self.router.get("/api/get-type-document-by-id", status_code=200, response_model=TypeDocumentModelOut)(
            ApiRest.get_type_document_by_id)
        self.router.put("/api/update-type-document", status_code=200, response_model=TypeDocumentModelOut)(
            ApiRest.update_type_document)
        self.router.delete("/api/delete-type-document", status_code=204, response_model=None)(
            ApiRest.delete_type_document)
        self.router.post("/api/create-country", status_code=201, response_model=CountryModelOut)(
            ApiRest.add_country)
        self.router.get("/api/get-all-countries", status_code=200, response_model=List[CountryModelOut])(
            ApiRest.get_all_countries)
        self.router.get("/api/get-country", status_code=200, response_model=CountryModelOut)(
            ApiRest.get_country_by_id)
        self.router.put("/api/update-country", status_code=200, response_model=CountryModelOut)(
            ApiRest.update_country)
        self.router.delete("/api/delete-country", status_code=204, response_model=None)(
            ApiRest.delete_country)
        self.router.post("/api/create-department", status_code=201, response_model=DepartmentModelOut)(
            ApiRest.add_department)
        self.router.get("/api/get-all-departments", status_code=200, response_model=List[DepartmentModelOut])(
            ApiRest.get_all_departments)
        self.router.get("/api/get-department", status_code=200, response_model=DepartmentModelOut)(
            ApiRest.get_department_by_id)
        self.router.put("/api/update-department", status_code=200, response_model=DepartmentModelOut)(
            ApiRest.update_department)
        self.router.delete("/api/delete-department", status_code=204, response_model=None)(
            ApiRest.delete_department)
        self.router.post("/api/create-municipality", status_code=201, response_model=MunicipalityModelOut)(
            ApiRest.add_municipality)
        self.router.get("/api/get-all-municipalities", status_code=200, response_model=List[MunicipalityModelOut])(
            ApiRest.get_all_municipalities)
        self.router.get("/api/get-municipality", status_code=200, response_model=MunicipalityModelOut)(
            ApiRest.get_municipality_by_id)
        self.router.put("/api/update-municipality", status_code=200, response_model=MunicipalityModelOut)(
            ApiRest.update_municipality)
        self.router.delete("/api/delete-municipality", status_code=204, response_model=None)(
            ApiRest.delete_municipality)
        self.router.post("/api/create-harvest", status_code=201, response_model=HarvestModelOut)(
            ApiRest.add_harvest)
        self.router.get("/api/get-all-harvests", status_code=200, response_model=List[HarvestModelOut])(
            ApiRest.get_all_harvests)
        self.router.get("/api/get-harvest", status_code=200, response_model=HarvestModelOut)(
            ApiRest.get_harvest_by_id)
        self.router.put("/api/update-harvest", status_code=200, response_model=HarvestModelOut)(
            ApiRest.update_harvest)
        self.router.delete("/api/delete-harvest", status_code=204, response_model=None)(
            ApiRest.delete_harvest)
        self.router.post("/api/create-crop", status_code=201, response_model=CropModelOut)(
            ApiRest.add_crop)
        self.router.get("/api/get-all-crops", status_code=200, response_model=List[CropModelOut])(
            ApiRest.get_all_crops)
        self.router.get("/api/get-crop", status_code=200, response_model=CropModelOut)(
            ApiRest.get_crop_by_id)
        self.router.put("/api/update-crop", status_code=200, response_model=CropModelOut)(
            ApiRest.update_crop)
        self.router.delete("/api/delete-crop", status_code=204, response_model=None)(
            ApiRest.delete_crop)
        self.router.get("/api/weeks-statisticas", status_code=200, response_model=List[dict])(
            ApiRest.weeks_statisticas)
        self.router.get("/api/most-planted-crop-by-municipality", status_code=200, response_model=List[dict])(
            ApiRest.most_planted_crop_by_municipality)
