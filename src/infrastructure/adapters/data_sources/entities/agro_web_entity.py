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
    gender_id = Column(Integer, ForeignKey('gender_agroweb.id_gender'))
    #type_document_id = Column(Integer, ForeignKey('type_document_agroweb.id_gender'))


class GenderEntity(Base):
    __tablename__ = 'gender_agroweb'
    id_gender = Column(Integer, primary_key=True, autoincrement=True)
    name_gender = Column(String(50), nullable=False)
    code_gender = Column(String(3), nullable=False, unique=True)


#class TypeDocumentEntity(Base):
#    __tablename__ = 'type_document_agroweb'
#    id_type_document = Column(Integer, primary_key=True, autoincrement=True)
#    name_type_document = Column(String(50), nullable=False)
#    code_type_document = Column(String(5), nullable=False, unique=True)

AuthenticationEntity.user = relationship(UserEntity, back_populates='auth')
UserEntity.auth = relationship(AuthenticationEntity, back_populates='user')
UserEntity.gender = relationship(GenderEntity, back_populates='users')
GenderEntity.users = relationship(UserEntity, back_populates='gender')
#TypeDocumentEntity.users = relationship(UserEntity, back_populates='typeDocument')
