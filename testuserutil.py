from userutil import UserUtil
import unittest
from datetime import datetime
import re


class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(str(user_id).startswith(str(datetime.now().year)[-2:]))

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("invalidemail.com"))
