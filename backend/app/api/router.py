from fastapi import APIRouter
from app.api.handlers import user

router = APIRouter()

router.include_router(user.user_router, prefix='/user', tags={"user"})
