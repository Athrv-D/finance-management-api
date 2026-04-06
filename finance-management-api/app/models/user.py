from sqlalchemy import Column, Integer,String,Boolean,Enum
from app.db.database import Base
from enum import Enum as Pyenum

class User_role(str,Pyenum):
    viewer = "viewer"
    admin = "admin"
    analyst = "analyst"

class User(Base):
    __tablename__ = "users"


    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    role = Column(Enum(User_role),default=(User_role.viewer))
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean,default=True)