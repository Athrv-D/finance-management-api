from pydantic import BaseModel,Field
from typing import Optional
from enum import Enum
from pydantic import validator
from datetime import date

class RecordType(str,Enum):
    income ="income"
    expense = "expense"

class RecordCreate(BaseModel):
    amount:float = Field(...,description="Transaction Amount")
    @validator("amount")
    def amount_positive(cls,v):
        if v<=0:
            raise ValueError("Amount must be positive")
        return v
    type:RecordType = Field(...)
    category:str = Field(...,description="e.g. food,salary,rent")
    date:date
    description:Optional[str]=None

class RecordResponse(RecordCreate):
    id:int
    class Config:
        from_attributes= True


        