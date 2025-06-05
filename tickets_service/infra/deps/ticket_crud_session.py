from tickets_service.infra.db.repositories import TicketCRUD
from .db_session import get_session
from sqlalchemy.orm import Session
from fastapi import Depends

def get_ticket_with_session(session: Session = Depends(get_session)) -> TicketCRUD:
    return TicketCRUD(session)