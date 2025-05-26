from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Numeric
from auth_service.infra.db import Base
from decimal import Decimal

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(10,2, asdecimal=True),
                                             nullable=False,
                                             default=Decimal("0.00")
                                             )