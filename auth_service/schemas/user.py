from pydantic import BaseModel, ConfigDict, Field, constr
from decimal import Decimal
from uuid import UUID

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    name: str = Field(..., min_length=3, max_length=10)
    password: constr(min_length=8) # type: ignore

class UserRead(UserBase):
    id: UUID
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)

class DepositRequest(BaseModel):
    value: Decimal

class BalanceRead(UserBase):
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)

