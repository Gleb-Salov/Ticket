from fastapi import APIRouter, Depends, status
from tickets_service.domain.schemas import TicketRead, TicketCreate
from tickets_service.infra.db import TicketCRUD
from tickets_service.infra.deps import get_ticket_with_session

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=TicketRead, status_code=status.HTTP_201_CREATED)
def ticket_create(
        ticket: TicketCreate,
        crud: TicketCRUD = Depends(get_ticket_with_session)
) -> TicketRead:
    return crud.ticket_create(ticket)
