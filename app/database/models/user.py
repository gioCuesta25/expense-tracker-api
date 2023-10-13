from typing import Optional
import uuid
from sqlmodel import Field, SQLModel
from pydantic import BaseModel, EmailStr

class UserBase(SQLModel):
    username: str = Field(unique=True)
    password: str
    email: EmailStr = Field(unique=True)
    inactive: bool = Field(default=False)


class User(UserBase, table=True):
    id: Optional[uuid.UUID] = Field(primary_key=True, default_factory=uuid.uuid4)


class UserCreate(UserBase):
    pass


class UserResponse(BaseModel):
    id: Optional[uuid.UUID]
    username: Optional[str]
    email: Optional[EmailStr]
    inactive: Optional[bool]


class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    inactive: Optional[bool] = None