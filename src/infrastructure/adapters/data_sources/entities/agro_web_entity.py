from sqlalchemy import (Column, Integer, String, Date, MetaData, ForeignKey, Boolean)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
metadata = MetaData()


class AuthenticationEntity(Base):
    __tablename__ = 'authentication_agroweb'
    id_auth = Column(Integer, primary_key=True, autoincrement=True)
    email_user_auth = Column(String(319), unique=True, nullable=False)
    password_auth = Column(String, nullable=False)
    disabled_auth = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('user_agroweb.id_user'))


class UserEntity(Base):
    __tablename__ = 'user_agroweb'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name_user = Column(String(50), nullable=False)
    lastname_user = Column(String(50), nullable=False)
    email_user = Column(String(319), unique=True, nullable=False)
    phone_user = Column(String(10), unique=True, nullable=False)
    id_document_user = Column(String(10), unique=True, nullable=False)
    birthdate_user = Column(Date)
    type_document_id = Column(Integer, ForeignKey('type_document_agroweb.id_type_document'))
    gender_id = Column(Integer, ForeignKey('gender_agroweb.id_gender'))
    municipality_id = Column(Integer, ForeignKey('municipality_agroweb.id_municipality'))


class GenderEntity(Base):
    __tablename__ = 'gender_agroweb'
    id_gender = Column(Integer, primary_key=True, autoincrement=True)
    name_gender = Column(String(50), nullable=False)
    code_gender = Column(String(5), nullable=False, unique=True)


class TypeDocumentEntity(Base):
    __tablename__ = 'type_document_agroweb'
    id_type_document = Column(Integer, primary_key=True, autoincrement=True)
    name_type_document = Column(String(50), nullable=False)
    code_type_document = Column(String(3), nullable=False, unique=True)


class MunicipalityEntity(Base):
    __tablename__ = 'municipality_agroweb'
    id_municipality = Column(Integer, primary_key=True, autoincrement=True)
    name_municipality = Column(String(50), nullable=False)
    code_municipality = Column(String(3), nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey('department_agroweb.id_department'))


class DepartmentEntity(Base):
    __tablename__ = 'department_agroweb'
    id_department = Column(Integer, primary_key=True, autoincrement=True)
    name_department = Column(String(50), nullable=False)
    code_department = Column(String(3), nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey('country_agroweb.id_country'))


class CountryEntity(Base):
    __tablename__ = 'country_agroweb'
    id_country = Column(Integer, primary_key=True, autoincrement=True)
    name_country = Column(String(50), nullable=False)
    code_country = Column(String(3), nullable=False, unique=True)


AuthenticationEntity.user = relationship(UserEntity, back_populates='auth')
UserEntity.auth = relationship(AuthenticationEntity, back_populates='user')
UserEntity.gender = relationship(GenderEntity, back_populates='users')
GenderEntity.users = relationship(UserEntity, back_populates='gender')
TypeDocumentEntity.users = relationship(UserEntity, back_populates='typeDocument')
UserEntity.typeDocument = relationship(TypeDocumentEntity, back_populates='users')
MunicipalityEntity.user = relationship(UserEntity, back_populates='municipality')
UserEntity.municipality = relationship(MunicipalityEntity, back_populates='user')
DepartmentEntity.municipality = relationship(MunicipalityEntity, back_populates='department')
MunicipalityEntity.department = relationship(DepartmentEntity, back_populates='municipality')
CountryEntity.department = relationship(DepartmentEntity, back_populates='country')
DepartmentEntity.country = relationship(CountryEntity, back_populates='department')
