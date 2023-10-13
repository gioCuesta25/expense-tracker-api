from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import BaseModel
import uuid


class CategoryBase(SQLModel):
    name: str = Field(max_length=50, unique=True)
    for_expenses: bool


class Category(CategoryBase, table=True):
    id: Optional[uuid.UUID] = Field(primary_key=True, default_factory=uuid.uuid4)


class CategoryResponse(BaseModel):
    id: Optional[uuid.UUID]
    name: Optional[str]
    for_expenses: Optional[bool]
