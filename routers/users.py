import sys
sys.path.append("..")

from typing import Optional
from fastapi import Depends,HTTPException, APIRouter
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_user_exception,get_current_user,get_password_hash, verify_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description":"User not found"}}    
)

models.Base.metadata.create_all(bind = engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str
    
@router.get("/")
async def read_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

@router.get("/getuser/{user_id}")
async def read_user_by_id(user_id : int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user_model is not None:
        return user_model
    
    return http_exception() 

@router.get("/getuser/")
async def read_user_id(user_id : int,db: Session = Depends(get_db)):
    user_model =  db.query(models.Users).filter(models.Users.id == user_id).first()

    if user_model is not None:
        return user_model
    
    return http_exception() 

@router.put("/password/")
async def modify_password(user_verification: UserVerification, user: dict = Depends(get_current_user),db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    
    if user_model is not None:
        if user_verification.username == user_model.username and verify_password(user_verification.password,user_model.hashed_password):
            
            user_model.hashed_password = get_password_hash(user_verification.new_password)
        db.add(user_model)
        db.commit()
        return successful_response()
    return http_exception()
@router.delete("/deleteuser/")
async def delete_user(user: dict = Depends(get_current_user),db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    
    if user_model is None:
        raise http_exception()
    
    db.query(models.Users).filter(models.Users.id == user.get("id")).delete()
    db.commit()
    
    return successful_response()
    
    
def http_exception():
    return HTTPException(status_code = 404,detail = "User not found")

def successful_response():
    return {
        'status' : 200,
        'transaction' : 'Successful'
    }