from fastapi import APIRouter, Depends, status
from auth_service.schemas import UserRead, UserCreate, BalanceRead, DepositRequest
from auth_service.use_cases import UserCRUD, get_user_crud
from auth_service.db import hash_user_password, get_common_deps, CommonDeps

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def user_create(
        user: UserCreate = Depends(hash_user_password),
        crud: UserCRUD = Depends(get_user_crud)
) -> UserRead:
    return crud.user_create(user)

@router.post("/deposit/", response_model=BalanceRead, status_code=status.HTTP_201_CREATED)
def user_deposit(
        request: DepositRequest,
        deps: CommonDeps = Depends(get_common_deps)
) -> BalanceRead:
    return deps.crud.dep(deps.user.name, request.value)