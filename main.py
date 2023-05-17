from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Role, User


app = FastAPI()


db: List[User] = [
    User(
        id=uuid4(),
        first_name="Satoru",
        last_name="Iwata",
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Donkey",
        last_name="Kong",
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return db
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )