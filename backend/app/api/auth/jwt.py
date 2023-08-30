from app.core.security import create_access_token, create_refresh_token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService


auth_router = APIRouter()


@auth_router.post('/login')
async def login(formData: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=formData.username, password=formData.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }
