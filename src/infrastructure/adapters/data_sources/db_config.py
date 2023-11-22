from sqlalchemy import (create_engine, func)
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from apscheduler.schedulers.background import BackgroundScheduler
from src.infrastructure.adapters.data_sources.entities import agro_web_entity
import os
from datetime import datetime, timedelta
import pytz

time_zone = pytz.timezone('America/Bogota')

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
    update_query = (session.query(agro_web_entity.CropEntity).
                    filter(((func.extract('week', agro_web_entity.
                                          CropEntity.approximate_durability_date) + agro_web_entity.
                           CropEntity.approximate_weeks_crop_durability - 1 < func.
                           extract('week', func.current_date())) & (func.current_date() >=
                                                                    (agro_web_entity.CropEntity.
                                                                     approximate_durability_date + func.make_interval
                                                                    (weeks=agro_web_entity.CropEntity.
                                                                     approximate_weeks_crop_durability))))
                           | ((func.extract('year', func.current_date()) >
                              func.extract('year', agro_web_entity.CropEntity.approximate_durability_date)) &
                              (func.extract('week', agro_web_entity.
                                            CropEntity.approximate_durability_date) + agro_web_entity.
                               CropEntity.approximate_weeks_crop_durability - 53 < func.
                               extract('week', func.current_date()))
                              )).
                    filter(agro_web_entity.CropEntity.activate == True).
                    update({agro_web_entity.CropEntity.activate: False}, synchronize_session=False))
    hora_actual = datetime.now(time_zone).strftime("%H:%M:%S")
    print(hora_actual)
    session.commit()
    session.close()
    print("We update crop statuses")


def update_weeks_crops_periodicals():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_weeks_crops, 'cron', hour=2, minute=0)
    scheduler.start()


Session = sessionmaker(bind=engine)
session = Session()
