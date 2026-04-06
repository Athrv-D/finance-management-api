from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import hash_password
from app.schemas.user_schema import UserCreate,UserLogin
from app.models.user import User
from app.services.auth_service import register_user,login_user
from app.core.security import create_token
from sqlalchemy import func

router = APIRouter()

@router.post("/register")
def register(data:UserCreate,db:Session=Depends(get_db)):

    existing_admin = db.query(User).filter(func.lower(User.role)=="admin").first()
    print("existing admin",existing_admin)

    if existing_admin:
        role = "viewer"

    else:
        role = "admin"
    user = User(name =data.name,
                email = data.email,
                password = hash_password(data.password),role = role)
    
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


    return{"message":" User created"}






@router.post("/login")
def login(data:UserLogin,db:Session=Depends(get_db)):
    user = login_user(db,data)

    if not user:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    token = create_token({
        "user_id":user.id,
        "role":user.role
    })
    return {"access_token":token}