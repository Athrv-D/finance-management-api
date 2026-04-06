from app.models.record import Record 

def create_record(db,data,user_id):
    record = Record(**data.dict(),user_id=user_id)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_records(db,user_id):
    return db.query(Record).all()