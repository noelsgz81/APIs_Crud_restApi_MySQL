from fastapi import APIRouter
from models.user import users
from config.db import conn
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

user = APIRouter()

@user.get('/users')
def get_users():
    result = conn.execute(users.select()).fetchall()
    result = dict((s[0], s[1:]) for s in result)
    print("Result: "+ str(result))
    return result

@user.post('/users')
def create_user(user: User):
    newUser = {"name": user.name, "email": user.email, "password": f.encrypt(user.password.encode("utf-8"))}
    result = conn.execute(users.insert().values(newUser))
    print(result)
    return "Hello Word"

# @user.get('/users')
# def helloWord():
#     return "Hello Word"

# @user.get('/users')
# def helloWord():
#     return "Hello Word"

# @user.get('/users')
# def helloWord():
#     return "Hello Word"