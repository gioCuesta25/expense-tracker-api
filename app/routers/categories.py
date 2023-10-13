from fastapi import APIRouter, Depends
from sqlmodel import Session, select, col
from database.database import engine
from database.models.categories import Category
from database.models.user import User
from utils.oauth import get_user_disabled_current

router = APIRouter(prefix='/categories', tags=["Categories"])


@router.get('/')
def get_categories(user: User = Depends(get_user_disabled_current)):
    with Session(engine) as session:
        statement = select(Category)
        categories = session.exec(statement=statement).all()
        return {"items": categories}
