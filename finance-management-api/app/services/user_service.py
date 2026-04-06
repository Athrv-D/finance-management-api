from app.models.user import User
from fastapi import HTTPException
from app.core.security import hash_password 


def create_user(db,user_data):
    existing = db.query(User).filter(User.email == user_data.email).first()

    if existing:
        raise  HTTPException(status_code=400,detail="Email already exists")
    data = user_data.dict()
    data["password"]=hash_password(data["password"])
    user = User(**data)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db,is_active:bool=None):
    query = db.query(User)
    if is_active is not None:
        query = query.filter(User.is_active==is_active)

    return query.all()


