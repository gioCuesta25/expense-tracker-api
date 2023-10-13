from sqlmodel import create_engine, SQLModel
import database.models.amounts
import database.models.categories
import database.models.user
from decouple import config

DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_USER = config("DB_USER")
DB_NAME = config("DB_NAME")
DB_PASSWORD = config("DB_PASSWORD")

POSTGRESQL_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


engine = create_engine(POSTGRESQL_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
