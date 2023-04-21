from flask import current_app
from datetime import datetime, timezone, timedelta
from services.user import UserService
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
