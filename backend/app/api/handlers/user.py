from TodoApp.backend.app.schemas.user_schema import UserAuth
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from app.services.user_service import UserService
import pymongo
from app.models.user_model import User


user_router = APIRouter()


@user_router.post('/create', summary="Create new user")
async def create_user(data: UserAuth):
    pass
