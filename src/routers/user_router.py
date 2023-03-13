
from uuid import UUID

from fastapi import APIRouter

from src.models.user import User
from src.services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])

service = UserService()


@router.get("/")
async def fetcg_users():
    return service.get_all_users()


@router.post("/")
async def create_user(user: User):
    user_id = service.save_user(user)
    return {"id": user_id}


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: UUID):
    service.delete_user(user_id)
