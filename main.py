from testuserutil import TestUserUtil
from testuserservice import TestUserService
from testuser import TestUser
from userutil import  UserUtil
from userservice import UserService
from user import User
from datetime import datetime, date
import unittest
import re

if __name__ == "__main__":
    # Create a new user
    user_id = UserUtil.generate_user_id()
    password = UserUtil.generate_password()
    email = UserUtil.generate_email("Alice", "Smith", "example.com")
    user = User(user_id, "Alice", "Smith", date(1998, 4, 23), password, email)


    # Add user to the service
    UserService.add_user(user)

    # Print user details
    print(user.get_details())

    # Find user by ID
    found_user = UserService.find_user(user_id)
    if found_user:
        print("User found:", found_user.get_details())

    # Update user email
    UserService.update_user(user_id, email="alice.smith@newdomain.com")
    print("Updated User:", UserService.find_user(user_id).get_details())

    # Delete user
    UserService.delete_user(user_id)
    print("User count after deletion:", UserService.get_number())

    unittest.main()
