from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str = Field(..., min_length=2)


class UserOut(BaseModel):
    id: str
    name: str
    username: str
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=2)
