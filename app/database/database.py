from sqlmodel import create_engine, SQLModel
import database.models.amounts
import database.models.categories
import database.models.user

DB_HOST = "peanut.db.elephantsql.com"
DB_PORT = 5432
DB_USER = "wijoudvp"
DB_NAME = "wijoudvp"
DB_PASSWORD = "b3rtaYTtaJmiMkC7Nuy9O3Az6cOaTM9T"

POSTGRESQL_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# POSTGRESQL_URL = 'postgresql://expense_tracker_db_x2d1_user:JtKqcniVo8l7uchhOTjxWWhlghpaP2e6@dpg-ckhmchcldqrs73bsb6ag-a.oregon-postgres.render.com/expense_tracker_db_x2d1'

engine = create_engine(POSTGRESQL_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
