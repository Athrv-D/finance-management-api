from fastapi import HTTPException,Depends,Header,Request
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt 
from app.db.database import get_db
from app.models.user import User

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def  create_token(data:dict):
    return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)


pwd_context = CryptContext(schemes=["bcrypt"])
security = HTTPBearer()





def get_current_user( credentials:HTTPAuthorizationCredentials=Depends(security),db:Session=Depends(get_db)):
    token= credentials.credentials

    try:
        payload  = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401,detail="Invalid token payload")
    except Exception as e:
        print('jwt error',e)
        raise HTTPException(status_code=401,detail="Invalid Token")
    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    

    return user
    
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password,hashed):
    return pwd_context.verify(password,hashed)

def role_allowed(allowed_roles:list):
    def role_checker(user =Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(status_code=403,detail="Access Denied")
        return user
    return role_checker