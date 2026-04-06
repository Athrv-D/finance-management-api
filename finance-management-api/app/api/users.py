from fastapi import APIRouter,Depends,HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.security import  get_current_user
from app.core.security import role_allowed
from app.db.database import get_db
from app.schemas.user_schema import UserCreate,UserAdd,UserResponse
from app.models.user import User
from app.services.user_service import create_user,get_users

router = APIRouter()

@router.post("/",response_model=UserResponse)
def add_user(user:UserAdd,db:Session=Depends(get_db),current_user=Depends(role_allowed(["admin"]))):
    return create_user(db,user)

@router.get("/",response_model=List[UserResponse])
def list_users(db:Session=Depends(get_db),is_active:bool=None,user=Depends(role_allowed(["admin","analyst"]))):
    return get_users(db,is_active)

@router.put("/{user_id}/status")
def update_user_status(
    user_id:int,
    is_active:bool,
    db:Session =Depends(get_db),
    current_user = Depends(role_allowed(["admin"]))
):
    user = db.query(User),filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
    user.is_active = is_active
    db.commit()
    db.refresh(user)
    return{"message":"User status update","is_active":user.is_active}
