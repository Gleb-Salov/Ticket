from sqlalchemy.orm import Session
from decimal import Decimal
from fastapi import HTTPException
from auth_service.domain import User
from auth_service.schemas import UserCreate, UserRead
from auth_service.utils import generate_id

class UserCRUD:
    def __init__(self, session: Session):
        self.session = session

    def user_create(self, user: UserCreate) -> UserRead:
        new_user = self.session.query(User).filter(User.name == user.name).first()
        if new_user:
            raise HTTPException(status_code=400, detail="User already exists")

        for _ in range(100):
            random_id = generate_id()
            if not self.session.query(User).filter(User.id == random_id).first():
                break
        else:
            raise Exception("Failed to generate unique ID")

        new_user = User(id=random_id, **user.dict())
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return UserRead.model_validate(new_user)

    def dep(self, user: User, value: int) -> UserRead:
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