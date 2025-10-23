from fastapi import FastAPI
from models import User, Role, Gender
from uuid import UUID, uuid4
from typing import List

app = FastAPI(name="User Management API")

db: List[User] = [
    User(id=UUID("c5bffb36-a7a9-48b5-b968-42c1d1204bec"),
         first_name="iicee",
         last_name="kiing",
         gender=Gender.male,
         role=[Role.admin, Role.user],
         age=25),
    
    User(id=UUID("76e6dd1f-6a6a-4f5f-81e8-26643b915ca6"),
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