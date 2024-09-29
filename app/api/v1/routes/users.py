from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.user_service import UserService
from app.schemas.user import CreateUserSchema, UpdateUserSchema
from app.core.response_handler import success_response
from app.core.security import hash_password, verify_password

router = APIRouter()
user_service = UserService()


# Read all users
@router.get("/")
async def read_users(db: AsyncSession = Depends(get_db)):
    try:
        results = await user_service.get_all_users(db)
        return success_response(
            http_status_code=200, data=results, message="List of users."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Create new user
@router.post("/")
async def create_user(user: CreateUserSchema):
    try:
        user.password = await hash_password(user.password)

        return success_response(
            http_status_code=status.HTTP_201_CREATED,
            data=user.model_dump(),
            message="User created successfully.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Read specific user
@router.get("/{user_id}")
async def read_user(user_id: str):
    return {"data": user_id}


# Update specific user
@router.put("/{user_id}")
async def update_user(user_id: str, user: UpdateUserSchema):
    return {"data": user_id}


# Delete specific user
@router.delete("/{user_id}")
async def delete_user(user_id: str):
    return {"data": user_id}
