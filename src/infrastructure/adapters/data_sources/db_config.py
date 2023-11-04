from sqlalchemy import (create_engine, update, extract, text)
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from apscheduler.schedulers.background import BackgroundScheduler
from src.infrastructure.adapters.data_sources.entities import agro_web_entity
import os
from datetime import datetime

load_dotenv()

host = os.getenv('HOST_NAME')
port = os.getenv('PORT')
database = os.getenv('DB_NAME')
user = os.getenv('USER_NAME')
schema = os.getenv("SCHEMA", 'public')
password = os.getenv('PASSWORD')
secret_key = os.getenv('SECRET_KEY')
algorithm = os.getenv('ALGORITHM')

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URL)


def create_tables():
    agro_web_entity.Base.metadata.create_all(engine)


def update_weeks_crops():

    update_query = text(
        f"UPDATE {'crop_agroweb'} SET {'activate'} = 'false' "
        f"WHERE EXTRACT(WEEK FROM {'approximate_durability_date'}) + "
        f"{'approximate_weeks_crop_durability'} < EXTRACT(WEEK FROM current_date) AND {'activate'} = 'true'"
    )
    hora_actual = datetime.now().strftime("%H:%M:%S")
    print(hora_actual)
    session.execute(update_query)
    session.commit()
    session.close()
    print("actualizar activate")


def update_weeks_crops_periodicals():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_weeks_crops, 'cron', hour=4, minute=0)
    scheduler.start()


Session = sessionmaker(bind=engine)
session = Session()
