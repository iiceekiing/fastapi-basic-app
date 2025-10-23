from fastapi import FastAPI
from models import User, Role, Gender
from uuid import uuid4
from typing import List

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="iicee",
         last_name="kiing",
         gender=Gender.male,
         role=[Role.admin, Role.user],
         age=25),
    
    User(id=uuid4(),
         first_name="dev",
         last_name="skript",
         gender=Gender.male,
         role=[Role.user], age=20)
]

@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}

@app.get("/api/v1/users")
async def get_users():
    return db