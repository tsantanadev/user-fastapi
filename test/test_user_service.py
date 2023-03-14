from unittest import TestCase
from uuid import UUID

from fastapi import HTTPException
from src.models.gender import Gender
from src.models.role import Role
from src.models.user import User

from src.services.user_service import UserService


class TestUserUservice(TestCase):

    def test_should_return_all_users(self):
        service = UserService()

        self.assertEqual(2, len(service.get_all_users()))

    def test_should_save_user_and_return_user_id(self):
        service = UserService()

        result = service.save_user(
            User(
                first_name="Thiaggo",
                last_name="Santana",
                gender=Gender.male,
                roles=[Role.student]
            )
        )

        self.assertEqual(3, len(service.get_all_users()))
        self.assertIsNotNone(result)

    def test_delete_should_remove_user(self):
        service = UserService()

        service.delete_user(UUID('aa471eec-cc3d-47ac-968f-162fae830eca'))

        self.assertEqual(1, len(service.get_all_users()))

    def test_delete_with_invalid_id_should_raise_exception(self):
        service = UserService()

        with self.assertRaises(HTTPException):
            service.delete_user('invalid')
