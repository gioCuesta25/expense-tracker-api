from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select, col
from database.database import engine
from database.models.user import User, UserResponse
from typing import List
from uuid import UUID
from utils.hashing import hash_password

router = APIRouter(tags=["Users"], prefix='/user')


@router.get('/', response_model=List[UserResponse])
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


@router.get('/{user_id}', response_model=UserResponse)
def get_user_by_id(user_id: UUID):
    with Session(engine) as session:
        statement = select(User).where(col(User.id) == user_id)
        db_user = session.exec(statement=statement)
        return db_user.first()


@router.post('/', response_model=UserResponse)
def create_user(user: User):
    with Session(engine) as session:
        user.password = hash_password(user.password)
        db_user = User.from_orm(user)
        session.add(db_user)
        session.commit()

        session.refresh(db_user)
        return db_user

# @router.patch('/{user_id}')
# def update_user(user_id: UUID , user: UserUpdate):
#     with Session(engine) as session:
#         db_user = session.exec(select(User).where(col(User.id) == user_id))
#         if not db_user:
#             raise HTTPException(status_code=404, detail='User not found')
#         user_data = user.dict(exclude_unset=True) # exclude_unset=True, exclude None values from de dict
#         for key, value in user_data.items():
#             setattr(db_user, key, value)
#         session.add(db_user)
#         session.commit()
#         session.refresh()
#         return db_user


@router.delete('/{user_id}')
def delete_user(user_id: UUID):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        session.delete(user)
        session.commit()
        return {'ok': True}
