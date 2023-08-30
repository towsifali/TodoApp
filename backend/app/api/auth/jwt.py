from datetime import datetime
from app.schemas.auth_schema import TokenPayload
from app.core.config import settings
from app.api.deps.user_deps import get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.auth_schema import TokenSchema
from app.models.user_model import User
from app.core.security import create_access_token, create_refresh_token
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from jose import jwt
from pydantic import ValidationError
from app.services.user_service import UserService


auth_router = APIRouter()


@auth_router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
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


@auth_router.post('/test_token', summary="Test if the token is valid", response_model=UserOut)
async def test_token(user: User = Depends(get_current_user)):
    return user


@auth_router.post('/refresh', summary="Refresh Token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[
                settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Tokent Expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user"
        )
    return user
