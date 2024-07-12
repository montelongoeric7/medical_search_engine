from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    is_admin: bool = False

class UserOut(UserBase):
    id: int
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

class InformationBase(BaseModel):
    title: str
    content: str
    published: bool = True

class InformationCreate(InformationBase):
    pass

class InformationOut(InformationBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ChatbotResponse(BaseModel):
    potential_causes: str

class SearchRequest(BaseModel):
    query:str


class ChatbotResponse2(BaseModel):
    potential_causes: str
    clinic: dict

class ClinicBase(BaseModel):
    name: str
    address: str
    phone: str
    email: EmailStr
    website: str
    services: str
    insurance: str
    cash: bool

class ClinicCreate(ClinicBase):
    pass

class ClinicOut(ClinicBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True





