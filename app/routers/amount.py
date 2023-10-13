from fastapi import APIRouter, Depends
from database.models.user import User
from database.models.amounts import AmountCreate, Expense, AmountResponse, Income
from database.database import engine
from utils.oauth import get_user_disabled_current
from sqlmodel import Session, select, col

router = APIRouter(prefix='/amounts', tags=["Amounts"])


@router.post('/expenses', response_model=AmountResponse)
def create_expense(expense: AmountCreate, user: User = Depends(get_user_disabled_current)):
    with Session(engine) as session:
        new_expense = Expense(user_id=user.id, category_id=expense.category_id, amount=expense.amount, date=expense.date, description=expense.description)
        session.add(new_expense)
        session.commit()
        session.refresh(new_expense)
        return new_expense


@router.get('/expenses')
def get_expenses(user: User = Depends(get_user_disabled_current)):
    with Session(engine) as session:
        statement = select(Expense).where(col(Expense.user_id) == user.id)
        expenses = session.exec(statement=statement).all()
        return {"items": expenses}


@router.post('/incomes', response_model=AmountResponse)
def create_income(income: AmountCreate, user: User = Depends(get_user_disabled_current)):
    with Session(engine) as session:
        new_income = Income(user_id=user.id, category_id=income.category_id, amount=income.amount, date=income.date, description=income.description)
        session.add(new_income)
        session.commit()
        session.refresh(new_income)
        return new_income


@router.get('/incomes')
def get_incomes(user: User = Depends(get_user_disabled_current)):
    with Session(engine) as session:
        statement = select(Income).where(col(Income.user_id) == user.id)
        expenses = session.exec(statement=statement).all()
        return {"items": expenses}
