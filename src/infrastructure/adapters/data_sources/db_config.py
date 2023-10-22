from sqlalchemy import (create_engine)
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from src.infrastructure.adapters.data_sources.entities import agro_web_entity
import os

load_dotenv()

host = os.getenv('HOST_NAME')
port = os.getenv('PORT')
database = os.getenv('DB_NAME')
user = os.getenv('USER_NAME')
schema = os.getenv("SCHEMA", 'public')
password = os.getenv('PASSWORD')

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URL)


def create_tables():
    agro_web_entity.Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
