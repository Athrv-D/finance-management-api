from app.models.user import User
from fastapi import HTTPException
from app.core.security import hash_password, verify_password
from sqlalchemy.orm import Session

 

def register_user(db:Session,data):
    existing_user =db.query(User).filter(User.email==data.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="User already exists")
    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def login_user(db:Session,data):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        return None
    if not verify_password(data.password,user.password):
        return None
    return user