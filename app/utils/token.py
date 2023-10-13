from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(config("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(payload: dict):
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_token(token: str):
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username = token_decode.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})