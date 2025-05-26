from typing import NamedTuple, TYPE_CHECKING
from auth_service.schemas import UserRead
from fastapi import Depends
from sqlalchemy.orm import Session
from auth_service.db.deps import get_session
from .auth_check import get_current_user

if TYPE_CHECKING:
    from auth_service.use_cases import UserCRUD

class CommonDeps(NamedTuple):
    crud: "UserCRUD"
    user: UserRead

def get_common_deps(
    session: Session = Depends(get_session),
    user: UserRead = Depends(get_current_user),
) -> CommonDeps:
    from auth_service.use_cases import UserCRUD
    crud = UserCRUD(session)
    return CommonDeps(crud=crud, user=user)
