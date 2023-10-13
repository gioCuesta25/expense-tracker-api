from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.token import verify_token
from database.database import engine
from sqlmodel import Session, select, col
from database.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    with Session(engine) as session:
        username: str = verify_token(token=token)
        user = session.exec(select(User.username, User.email, User.id, User.inactive).where(
            col(User.username) == username)).one_or_none()
        if not user:
            raise HTTPException(status_code=401, detail="Could not validate credentials", headers={
                                "WWW-Authenticate": "Bearer"})
        return user


def get_user_disabled_current(user: User = Depends(get_current_user)):
    if user.inactive:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user
