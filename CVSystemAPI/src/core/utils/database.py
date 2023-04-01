from sqlalchemy import create_engine
from src.constants import DATABASE_URL


class DB:
    __instance = None

    def __init__(self):
        if (DB.__instance is not None):
            raise Exception("Instance of this class already exists, use DB.create()")
        else:
            DB.__instance = self
        self.engine = self.create_engine()

    @staticmethod
    def get_instance():
        if (DB.__instance is None):
            return DB()

        return DB.__instance

    def create_engine(self):
        return create_engine(
            DATABASE_URL)
