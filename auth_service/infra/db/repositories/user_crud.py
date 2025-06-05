from sqlalchemy.orm import Session
from fastapi import HTTPException
from auth_service.domain import User
from auth_service.schemas import UserCreate, UserRead
from decimal import Decimal

class UserCRUD:
    def __init__(self, session: Session):
        self.session = session

    def user_create(self, user: UserCreate) -> UserRead:
        new_user = self.session.query(User).filter(User.name == user.name).first()
        if new_user:
            raise HTTPException(status_code=400, detail="User already exists")

        new_user = User(**user.model_dump())
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return UserRead.model_validate(new_user)

    def dep(self, user: User, value: Decimal) -> UserRead:
        balance_owner = self.session.query(User).filter(User.id == user.id).first()
        if not balance_owner:
            raise HTTPException(status_code=404, detail="User doesn't exist")
        if value <= 0:
            raise HTTPException(status_code=400, detail="Value must be greater than 0")
        balance_owner.balance = Decimal(balance_owner.balance + value)
        self.session.add(balance_owner)
        self.session.commit()
        self.session.refresh(balance_owner)

        return UserRead.model_validate(balance_owner)