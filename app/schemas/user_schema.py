from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    role: str
    user_id: str


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    reporting_manager_id: Optional[UUID] = None