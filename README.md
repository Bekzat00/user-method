# User Management System  

## **Project Overview**
This project is an Object-Oriented Python application that manages user records. It consists of three main classes:  
- `User` – Represents an individual user.  
- `UserService` – Manages user records using class methods.  
- `UserUtil` – Provides utility functions like ID and password generation.  

## **Features**
- Create and manage users.
- Generate unique user IDs and secure passwords.
- Validate emails and enforce password strength.
- Perform CRUD operations on users (Create, Read, Update, Delete).
- Unit tests to ensure code reliability.

## **Project Structure**
Class Descriptions
User Class
Represents an individual user with the following attributes:

user_id (int): Unique identifier.
name (str): First name.
surname (str): Last name.
email (str): Email address.
password (str): Secure password.
birthday (datetime): User's birth date.
Methods:

get_details(): Returns formatted user details.
get_age(): Calculates and returns the user’s age.
UserService Class
Manages users using a class attribute (users dictionary).

Class Methods:

add_user(user): Adds a user.
find_user(user_id): Searches for a user by ID.
delete_user(user_id): Deletes a user by ID.
update_user(user_id, **kwargs): Updates user details.
get_number(): Returns total number of users.
UserUtil Class
Provides utility functions for user management.

Static Methods:

generate_user_id(): Generates a unique 9-digit user ID.
generate_password(): Generates a strong password.
is_strong_password(password): Validates password strength.
generate_email(name, surname, domain): Creates an email.
validate_email(email): Validates an email format.

Usage Examples
1. Creating and Adding a User
from datetime import date
from user import User
from userservice import UserService
from userutil import UserUtil

# Generate user details
user_id = UserUtil.generate_user_id()
password = UserUtil.generate_password()
email = UserUtil.generate_email("Alice", "Smith", "example.com")
birthday = date(1998, 4, 23)

# Create user and add to service
user = User(user_id, "Alice", "Smith", birthday, password, email)
UserService.add_user(user)


Output

ID: 240123456, Name: Alice Smith, Email: alice.smith@example.com, Birthday: 1998-04-23

Finding a Users
found_user = UserService.find_user(user_id)
if found_user:
    print("User found:", found_user.get_details())
Output
User found: ID: 240123456, Name: Alice Smith, Email: alice.smith@example.com, Birthday: 1998-04-23

Uploating a user's Email
UserService.update_user(user_id, email="alice.smith@newdomain.com")
print("Updated User:", UserService.find_user(user_id).get_details())
output
User count after deletion: 0

