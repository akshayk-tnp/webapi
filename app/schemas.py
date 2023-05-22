from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    firstName:str
    lastName:str
    email: EmailStr
    password: str
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class ChartData(BaseModel):
    labels: str
    value: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

class Post(BaseModel):
    content: str
    created_at: datetime
    topic:str
    owner_id:str
    owner:UserOut


    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    content: str
    topic:str
    created_at: datetime


    class Config:
        orm_mode = True