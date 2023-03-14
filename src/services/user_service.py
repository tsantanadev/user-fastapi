from typing import List
from uuid import UUID

from fastapi import HTTPException

from src.models.gender import Gender
from src.models.role import Role
from src.models.user import User


class UserService:

    def __init__(self):
        self.__db: List[User] = [
            User(
                id="aa471eec-cc3d-47ac-968f-162fae830eca",
                first_name="Leticia",
                last_name="Gontijo",
                gender=Gender.female,
                roles=[Role.admin]
            ),
            User(
                id="6c95fac5-390c-4b26-a637-7cff70dc9055",
                first_name="Thiago",
                last_name="Santana",
                gender=Gender.male,
                roles=[Role.student]
            )
        ]

    def get_all_users(self):
        return self.__db

    def save_user(self, user: User):
        self.__db.append(user)
        return user.id

    def delete_user(self, user_id: UUID):
        for user in self.__db:
            if user.id == user_id:
                self.__db.remove(user)
                return

        raise HTTPException(
            status_code=404,
            detail=f"User with id: {user_id} does not exists"
        )
