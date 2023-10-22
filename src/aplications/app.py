from fastapi import FastAPI
from src.infrastructure.contrrollers.routers import ApiRouter
from src.infrastructure.adapters.data_sources.db_config import create_tables, database

api_router = ApiRouter()


class App:
    def __init__(self):
        self.app = FastAPI()
        self.configure()

    def configure(self):
        create_tables()
        self.app.include_router(api_router.router)

    @staticmethod
    async def startup():
        await database.connect()

    @staticmethod
    async def shutdown():
        await database.disconnect()


ap = App()
