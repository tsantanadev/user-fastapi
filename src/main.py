from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id="aa471eec-cc3d-47ac-968f-162fae830eca",
        first_name="Leticia",
        last_name="Gontijo",
        gender=Gender.female,
        roles=[Role.admin]
    ),
    User(
        id="6c95fac5-390c-4b26-a637-7cff70dc9055",
        first_name="Thiaggo",
        last_name="Santana",
        gender=Gender.male,
        roles=[Role.student]
    )
]


@app.get("/")
async def root():
    return {"Ola": "Mundo"}


@app.get("/api/v1/users")
async def fetcg_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}", status_code=204)
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )
