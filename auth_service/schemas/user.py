from pydantic import BaseModel, ConfigDict, Field, constr
from decimal import Decimal

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    name: str = Field(..., min_length=3, max_length=10)
    password: str = constr(min_length=8)

class UserRead(UserBase):
    id: int
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)

class DepositRequest(BaseModel):
    value: Decimal

class BalanceRead(UserBase):
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)

