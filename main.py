# Unit Testing
import unittest
from user import User
from datetime import datetime
import re


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(240000001, "John", "Doe", datetime.date(2000, 1, 1))

    def test_get_details(self):
        self.assertIn("John Doe", self.user.get_details())

    def test_get_age(self):
        self.assertEqual(self.user.get_age(), datetime.date.today().year - 2000)
