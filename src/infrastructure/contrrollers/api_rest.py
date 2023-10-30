from fastapi import Depends
from src.domain.uses_cases.user_use_cases import UserModelIn
from src.domain.uses_cases.gender_use_cases import GenderModelIn
from src.domain.uses_cases.type_document_use_cases import TypeDocumentModelIn
from src.domain.uses_cases.country_use_case import CountryModelIn
from src.domain.uses_cases.department_use_case import DepartmentModelIn
from src.domain.uses_cases.municipality_use_case import MunicipalityModelIn
from src.domain.uses_cases.user_use_cases import AuthenticationModel
from src.domain.uses_cases.user_use_cases import UserUseCase
from src.domain.uses_cases.gender_use_cases import GenderUseCase
from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from src.domain.uses_cases.type_document_use_cases import TypeDocumentUseCase
from src.domain.uses_cases.country_use_case import CountryUseCase
from src.domain.uses_cases.municipality_use_case import MunicipalityUseCase
from src.domain.uses_cases.department_use_case import DepartmentUseCase
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer("/token")
user_use_case = UserUseCase()
gender_use_case = GenderUseCase()
type_document_use_case = TypeDocumentUseCase()
country_use_case = CountryUseCase()
department_use_case = DepartmentUseCase()
municipality_use_case = MunicipalityUseCase()


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
