from werkzeug.security import generate_password_hash
from models import User
from .base import Factory

class UserFactory(Factory):
    def __init__(self):
        self.model = User


    def define_attributes(self):
        return {
            "username": self.faker().profile()["username"],
            "password": generate_password_hash("password")
        }
