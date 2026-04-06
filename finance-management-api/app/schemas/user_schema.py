from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    name:str 
    email:str = Field(...,description="e.g. vvvv@gmail.com")
    password:str
    # role:str = Field(...,description=" e.g. viewer,admin,analyst")

class UserAdd(BaseModel):
    name:str
    email:str
    password:str
    role:str

class UserLogin(BaseModel):
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    role:str
    is_active:bool

    class Config:
        from_attributes =True
