from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict,
from uuid import UUID, uuid4
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other" 
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"
    student = "student"
    teacher = "teacher"
    
    
class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    midle_name: Optional[str] = None
    gender: Gender
    role: List[Role]
    age: Optional[int] = None

app = FastAPI()
