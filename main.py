from typing import List
from uuid import uuid4
from fastapi import FastAPI

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
def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
def fetch_users():
    return db