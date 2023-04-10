from flask import current_app, session
from datetime import datetime, timezone, timedelta
import jwt

def create_token(user):
    if user['username'] != 'admin':
        return None

    payload = {
        'sub': user['username'],
        'username': user['username'],
        'exp': datetime.now(tz=timezone.utc) + timedelta(days=1)
    }
    token = jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm=current_app.config['JWT_ENCODING_ALG'])
    return token

def set_user_session(token):
    user = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=current_app.config['JWT_ENCODING_ALG'])
    session['user'] = user
