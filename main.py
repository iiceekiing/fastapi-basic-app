from fastapi import FastAPI
from models import User, Role, Gender
from uuid import uuid4
from typing import List

app = FastAPI()

db = List[User] = [
    User(id=uuid4(),
         first_name="iicee",
         last_name="kiing",
         gender"male", 
         role=[Role.admin, Role.user], age=25),
    
        User(id=uuid4(),
         first_name="dev",
         last_name="skript",
         gender"male", 
         role=[Role.user], age=20),
]
