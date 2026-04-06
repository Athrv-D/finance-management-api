from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.security import role_allowed
from app.db.database import get_db
from app.services.dashboard_service import get_summary




router = APIRouter()

@router.get("/")
def summary(db:Session = Depends(get_db),user =Depends(role_allowed(["viewer","admin","analyst"]))):
    # role_allowed(user.role,["viewer","admin","analyst"])
    return get_summary(db)

