from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import BaseModel
import uuid
from datetime import datetime


class AmountBase(SQLModel):
    amount: int
    description: Optional[str] = Field(max_length=200)
    date: datetime
    category_id: uuid.UUID = Field(foreign_key="category.id")


class Expense(AmountBase, table=True):
    id: Optional[uuid.UUID] = Field(primary_key=True, default_factory=uuid.uuid4)
    user_id: uuid.UUID = Field(foreign_key="user.id")


class Income(AmountBase, table=True):
    id: Optional[uuid.UUID] = Field(primary_key=True, default_factory=uuid.uuid4)
    user_id: uuid.UUID = Field(foreign_key="user.id")


class AmountCreate(AmountBase):
    pass


class AmountResponse(BaseModel):
    id: Optional[uuid.UUID]
    amount: Optional[int]
    description: Optional[str]
    category_id: Optional[uuid.UUID]
