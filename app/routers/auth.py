from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database.database import engine
from sqlmodel import Session, select, col
from database.models.user import User
from utils.hashing import verify_password
from utils.token import create_access_token

router = APIRouter(prefix="/token", tags=["Token"])


@router.post('/')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(username=form_data.username,
                             password=form_data.password)
    access_token = create_access_token(payload={"username": user.username, "email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


def authenticate_user(username: str, password: str):
    with Session(engine) as session:
        statement = select(User).where(col(User.username) == username)
        user = session.exec(statement=statement).one_or_none()
        if not user:
            raise HTTPException(status_code=401, detail="Could not validate credentials", headers={
                                "WWW-Authenticate": "Bearer"})
        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Could not validate credentials", headers={
                                "WWW-Authenticate": "Bearer"})
        return user
