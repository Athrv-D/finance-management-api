from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey
from app.db.database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer,primary_key=True,index=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    user_id = Column(Integer,ForeignKey("users.id"))
    description = Column(String)