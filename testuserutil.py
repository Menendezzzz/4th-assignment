import unittest
from user import User
from userservice import UserService
from datetime import datetime
import re

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(240000002, "Jane", "Doe", datetime.date(1995, 5, 5))
        UserService.add_user(self.user)

    def test_add_and_find_user(self):
        self.assertEqual(UserService.find_user(240000002), self.user)

    def test_delete_user(self):
        UserService.delete_user(240000002)
        self.assertIsNone(UserService.find_user(240000002))

    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 1)