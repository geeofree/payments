from werkzeug.security import generate_password_hash
from models import User
from .factory import Factory

class UserFactory(Factory):
    model = User

    def define_attributes(self):
        return {
            "username": self.faker.profile()["username"],
            "password": generate_password_hash("password")
        }
