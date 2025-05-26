from fastapi import APIRouter, Depends, status
from auth_service.schemas import UserRead, UserCreate, DepositRequest
from auth_service.infra import UserCRUD, get_user_crud, hash_user_password, get_common_deps, CommonDeps

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def user_create(
        user: UserCreate = Depends(hash_user_password),
        crud: UserCRUD = Depends(get_user_crud)
) -> UserRead:
    return crud.user_create(user)

@router.post("/deposit/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def user_deposit(
        request: DepositRequest,
        deps: CommonDeps = Depends(get_common_deps)
) -> UserRead:
    return deps.crud.dep(deps.user, request.value)