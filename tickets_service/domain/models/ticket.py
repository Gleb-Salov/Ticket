from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, DateTime, ForeignKey
from tickets_service.infra.db import Base
from decimal import Decimal
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[UUID] = mapped_column(primary_key=True, index=True, default=uuid4)
    type: Mapped[str] = mapped_column()
    title: Mapped[Optional[str]] = mapped_column(unique=False, nullable=True)
    purchase_status: Mapped[bool] = mapped_column(nullable=False, default=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2, asdecimal=True),
                                            nullable=False,
                                            default=Decimal("0.00"))


class TicketPurchase(Base):
    __tablename__ = "ticket_purchases"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(nullable=False, index=True)
    ticket_id: Mapped[UUID] = mapped_column(ForeignKey("tickets.id"), index=True)
    purchase_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    ticket: Mapped["Ticket"] = relationship("Ticket")