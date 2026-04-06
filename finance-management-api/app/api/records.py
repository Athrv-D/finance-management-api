from fastapi import APIRouter,Depends,Query,Header,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import List
from app.core.security import get_current_user
from app.models.record import Record
from app.core.security import role_allowed
from app.schemas.record_schema import RecordCreate,RecordResponse
from app.services.record_service import get_records,create_record

router = APIRouter()

@router.post("/",response_model=RecordResponse)

def add_records(record:RecordCreate,db:Session=Depends(get_db),user=Depends(role_allowed(["admin"]))):
    return create_record(db,record,user.id)


@router.get("/",response_model=List[RecordResponse])
def list_records(
    type:str=Query(None),
    db:Session=Depends(get_db),user=Depends(role_allowed(["admin","analyst"]))):
    if type:
        return db.query(Record).filter(Record.type==type).all()
    return get_records(db,user.id)

@router.put("/{id}")

def update_record(id:int,data:RecordCreate,db:Session=Depends(get_db),user=Depends(role_allowed(["admin"]))):

    record=db.query(Record).filter(Record.id==id).first()

    if not record:
        raise HTTPException(status_code=404,detail="Record not found")
    
    record.amount = data.amount
    record.type = data.type
    record.category = data.category
    record.date=data.date

    db.commit()
    db.refresh(record)
    return record


@router.delete("/{id}")

def delete_record(id:int,db:Session=Depends(get_db),user=Depends(role_allowed(["admin"]))):

    record = db.query(Record).filter(Record.id==id).first()

    if not record:
        raise HTTPException(status_code=404,detail="Record not found")
    
    db.delete(record)
    db.commit()
    return {"message":"Deleted successfully"}

@router.get("/filter")
def filter_record(category:str=None,type:str=None,date:str=None,db:Session=Depends(get_db),user = Depends(role_allowed(["admin","analyst"]))):

    query = db.query(Record)

    if category:
        query = query.filter(Record.category==category)

    if type:
        query = query.filter(Record.type==type)

    if date:
        query = query.filter(Record.date == date)

    return query.all()
