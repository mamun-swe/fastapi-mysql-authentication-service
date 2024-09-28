from fastapi import APIRouter, status, HTTPException
from app.schemas.user import CreateUserSchema, UpdateUserSchema
from app.core.response_handler import success_response
from app.core.security import hash_password, verify_password

router = APIRouter()


# Read all users
@router.get("/")
async def read_users():
    try:
        return success_response(http_status_code=200, data=[], message="List of users.")
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
