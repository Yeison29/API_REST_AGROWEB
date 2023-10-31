from fastapi import Depends
from src.domain.uses_cases.user_use_cases import UserModelIn, UserUseCase
from src.domain.uses_cases.gender_use_cases import GenderModelIn, GenderUseCase
from src.domain.uses_cases.type_document_use_cases import TypeDocumentModelIn, TypeDocumentUseCase
from src.domain.uses_cases.country_use_cases import CountryModelIn, CountryUseCase
from src.domain.uses_cases.department_use_cases import DepartmentModelIn, DepartmentUseCase
from src.domain.uses_cases.municipality_use_cases import MunicipalityModelIn, MunicipalityUseCase
from src.domain.uses_cases.user_use_cases import AuthenticationModel, AuthenticationUseCase
from src.domain.uses_cases.crop_use_cases import CropModelIn, CropUseCase
from src.domain.uses_cases.haverst_use_cases import HarvestModelIn, HarvestUseCase
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer("/token")
user_use_case = UserUseCase()
gender_use_case = GenderUseCase()
type_document_use_case = TypeDocumentUseCase()
country_use_case = CountryUseCase()
department_use_case = DepartmentUseCase()
municipality_use_case = MunicipalityUseCase()
crop_use_case = CropUseCase()
harvest_use_case = HarvestUseCase()


class ApiRest:

    @staticmethod
    async def token(form_data: OAuth2PasswordRequestForm = Depends()):
        response = await AuthenticationUseCase.authenticate_user(form_data.password, form_data.username)
        return response

    @staticmethod
    async def add_user(user: UserModelIn, auth: AuthenticationModel):
        response = await user_use_case.add_user(user, auth)
        return response

    @staticmethod
    async def get_all_users(token: str = Depends(oauth2_scheme)):
        response = await user_use_case.get_all_users(token)
        return response

    @staticmethod
    async def get_user_by_id(id_user: int,  token: str = Depends(oauth2_scheme)):
        response = await user_use_case.get_user_by_id(id_user, token)
        return response

    @staticmethod
    async def update_user(id_user: int, user: UserModelIn, token: str = Depends(oauth2_scheme)):
        response = await user_use_case.update_user(id_user, user, token)
        return response

    @staticmethod
    async def delete_user(id_user: int, token: str = Depends(oauth2_scheme)):
        response = await user_use_case.delete_user(id_user, token)
        return response

    @staticmethod
    async def add_gender(gender: GenderModelIn,  token: str = Depends(oauth2_scheme)):
        response = await gender_use_case.add_gender(gender, token)
        return response

    @staticmethod
    async def get_all_genders():
        response = await gender_use_case.get_all_genders()
        return response

    @staticmethod
    async def get_gender_by_id(id_gender: int, token: str = Depends(oauth2_scheme)):
        response = await gender_use_case.get_gender_by_id(id_gender, token)
        return response

    @staticmethod
    async def update_gender(id_gender: int, gender: GenderModelIn, token: str = Depends(oauth2_scheme)):
        response = await gender_use_case.update_gender(id_gender, gender, token)
        return response

    @staticmethod
    async def delete_gender(id_gender: int, token: str = Depends(oauth2_scheme)):
        response = await gender_use_case.delete_gender(id_gender, token)
        return response

    @staticmethod
    async def add_type_document(type_document: TypeDocumentModelIn, token: str = Depends(oauth2_scheme)):
        response = await type_document_use_case.add_type_document(type_document, token)
        return response

    @staticmethod
    async def get_all_type_documents():
        response = await type_document_use_case.get_all_type_documents()
        return response

    @staticmethod
    async def get_type_document_by_id(id_type_document: int, token: str = Depends(oauth2_scheme)):
        response = await type_document_use_case.get_type_document_by_id(id_type_document, token)
        return response

    @staticmethod
    async def update_type_document(id_type_document: int, type_document: TypeDocumentModelIn,
                                   token: str = Depends(oauth2_scheme)):
        response = await type_document_use_case.update_type_document(id_type_document, type_document, token)
        return response

    @staticmethod
    async def delete_type_document(id_type_document: int, token: str = Depends(oauth2_scheme)):
        response = await type_document_use_case.delete_type_document(id_type_document, token)
        return response

    @staticmethod
    async def add_country(country: CountryModelIn, token: str = Depends(oauth2_scheme)):
        response = await country_use_case.add_country(country, token)
        return response

    @staticmethod
    async def get_all_countries():
        response = await country_use_case.get_all_countries()
        return response

    @staticmethod
    async def get_country_by_id(id_country: int, token: str = Depends(oauth2_scheme)):
        response = await country_use_case.get_country_by_id(id_country, token)
        return response

    @staticmethod
    async def update_country(id_country: int, country: CountryModelIn, token: str = Depends(oauth2_scheme)):
        response = await country_use_case.update_country(id_country, country, token)
        return response

    @staticmethod
    async def delete_country(id_country: int, token: str = Depends(oauth2_scheme)):
        response = await country_use_case.delete_country(id_country, token)
        return response

    @staticmethod
    async def add_department(department: DepartmentModelIn, token: str = Depends(oauth2_scheme)):
        response = await department_use_case.add_department(department, token)
        return response

    @staticmethod
    async def get_all_departments():
        response = await department_use_case.get_all_departments()
        return response

    @staticmethod
    async def get_department_by_id(id_department: int, token: str = Depends(oauth2_scheme)):
        response = await department_use_case.get_department_by_id(id_department, token)
        return response

    @staticmethod
    async def update_department(id_department: int, department: DepartmentModelIn, token: str = Depends(oauth2_scheme)):
        response = await department_use_case.update_department(id_department, department, token)
        return response

    @staticmethod
    async def delete_department(id_department: int, token: str = Depends(oauth2_scheme)):
        response = await department_use_case.delete_department(id_department, token)
        return response

    @staticmethod
    async def add_municipality(municipality: MunicipalityModelIn, token: str = Depends(oauth2_scheme)):
        response = await municipality_use_case.add_municipality(municipality, token)
        return response

    @staticmethod
    async def get_all_municipalities():
        response = await municipality_use_case.get_all_municipalities()
        return response

    @staticmethod
    async def get_municipality_by_id(id_municipality: int, token: str = Depends(oauth2_scheme)):
        response = await municipality_use_case.get_municipality_by_id(id_municipality, token)
        return response

    @staticmethod
    async def update_municipality(id_municipality: int, municipality: MunicipalityModelIn,
                                  token: str = Depends(oauth2_scheme)):
        response = await municipality_use_case.update_municipality(id_municipality, municipality, token)
        return response

    @staticmethod
    async def delete_municipality(id_municipality: int, token: str = Depends(oauth2_scheme)):
        response = await municipality_use_case.delete_municipality(id_municipality, token)
        return response

    @staticmethod
    async def add_crop(crop: CropModelIn, token: str = Depends(oauth2_scheme)):
        response = await crop_use_case.add_crop(crop, token)
        return response

    @staticmethod
    async def get_all_crops(token: str = Depends(oauth2_scheme)):
        response = await crop_use_case.get_all_crops(token)
        return response

    @staticmethod
    async def get_crop_by_id(id_crop: int, token: str = Depends(oauth2_scheme)):
        response = await crop_use_case.get_crop_by_id(id_crop, token)
        return response

    @staticmethod
    async def update_crop(id_crop: int, crop: CropModelIn, token: str = Depends(oauth2_scheme)):
        response = await crop_use_case.update_crop(id_crop, crop, token)
        return response

    @staticmethod
    async def delete_crop(id_crop: int, token: str = Depends(oauth2_scheme)):
        response = await crop_use_case.delete_crop(id_crop, token)
        return response

    @staticmethod
    async def add_harvest(harvest: HarvestModelIn, token: str = Depends(oauth2_scheme)):
        response = await harvest_use_case.add_harvest(harvest, token)
        return response

    @staticmethod
    async def get_all_harvests(token: str = Depends(oauth2_scheme)):
        response = await harvest_use_case.get_all_harvests(token)
        return response

    @staticmethod
    async def get_harvest_by_id(id_harvest: int, token: str = Depends(oauth2_scheme)):
        response = await harvest_use_case.get_harvest_by_id(id_harvest, token)
        return response

    @staticmethod
    async def update_harvest(id_harvest: int, harvest: HarvestModelIn, token: str = Depends(oauth2_scheme)):
        response = await harvest_use_case.update_harvest(id_harvest, harvest, token)
        return response

    @staticmethod
    async def delete_harvest(id_harvest: int, token: str = Depends(oauth2_scheme)):
        response = await harvest_use_case.delete_harvest(id_harvest, token)
        return response
