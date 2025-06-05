from typing import NamedTuple
from fastapi import Depends
from .auth_check import get_current_user
from .user_crud_session import get_user_crud
from auth_service.infra.db.repositories.user_crud import UserCRUD
from auth_service.domain import User

class CommonDeps(NamedTuple):
    crud: UserCRUD
    user: User

def get_common_deps(
    user: User = Depends(get_current_user),
    crud: UserCRUD = Depends(get_user_crud),
) -> CommonDeps:
    return CommonDeps(crud=crud, user=user)
