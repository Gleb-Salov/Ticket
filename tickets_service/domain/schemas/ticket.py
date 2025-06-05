from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from uuid import UUID
from decimal import Decimal

class TicketBase(BaseModel):
    type: str = Field(..., max_length=20)
    title: Optional[str] = None
    price: Decimal

class TicketCreate(TicketBase):
    pass

class TicketRead(TicketBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
