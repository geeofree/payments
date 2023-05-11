from flask import current_app, g
from datetime import datetime, timezone, timedelta
from .user import UserService
import jwt

class AuthService:
    @staticmethod
    def create_token(user):
        validated_user = UserService.validate_user(user['username'], user['password'])

        if validated_user == None:
            return None

        payload = {
            'sub': validated_user['username'],
            'user': validated_user,
            'exp': datetime.now(tz=timezone.utc) + timedelta(days=1)
        }

        token = jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm=current_app.config['JWT_ENCODING_ALG'])
        return token

    @staticmethod
    def decode_token(token):
        return jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=current_app.config['JWT_ENCODING_ALG'])


    @staticmethod
    def has_role(role):
        return role in g.user.get("user", {}).get("roles")


    @staticmethod
    def get_subordinate_role():
        if AuthService.has_role("master"):
            return "admin"
        elif AuthService.has_role("admin"):
            return "biller"
