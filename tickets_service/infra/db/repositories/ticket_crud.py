from sqlalchemy.orm import Session
from tickets_service.domain.schemas import TicketRead, TicketCreate
from tickets_service.domain.models import Ticket

class TicketCRUD:
    def __init__(self, session: Session):
        self.session = session

    def ticket_create(self, ticket: TicketCreate) -> TicketRead:
        new_ticket =  Ticket(**ticket.model_dump())
        self.session.add(new_ticket)
        self.session.commit()
        self.session.refresh(new_ticket)
        return TicketRead.model_validate(new_ticket)