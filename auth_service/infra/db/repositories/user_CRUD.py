from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from auth_service.db.deps import get_session
from auth_service.models import User
from auth_service.schemas import UserCreate, UserRead, BalanceRead
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

    def dep(self, username: str, value: int) -> BalanceRead:
        balance_owner = self.session.query(User).filter(User.name == username).first()
        if not balance_owner:
            raise HTTPException(status_code=400, detail="User doesn't exist")
        elif value <= 0:
            raise HTTPException(status_code=400, detail="Value must be greater than 0")
        balance_owner.balance += value
        self.session.add(balance_owner)
        self.session.commit()
        self.session.refresh(balance_owner)

        return BalanceRead.model_validate(balance_owner)


def get_user_crud(session: Session = Depends(get_session)) -> UserCRUD:
    return UserCRUD(session = session)