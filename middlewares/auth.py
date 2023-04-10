from flask import session, request, current_app
from utils.http import json_response
from services.auth import AuthService
import jwt

def validate_token():
    """
    Validates the bearer token and sets the current user session.
    """
    authorization = request.headers.get("authorization")

    if authorization == None:
        return json_response("No authorization header given.", 400)

    try:
        scheme, token = authorization.split()

        if scheme.lower() != "bearer":
            return json_response("Authorization header only accepts 'Bearer' scheme", 400)

        AuthService.set_user_session(token)
    except jwt.DecodeError as decode_error:
        return json_response("Could not decode token: {}".format(decode_error), 406)
    except jwt.ExpiredSignatureError:
        return json_response("Token is expired. Please sign-in again.", 406)
    except ValueError:
        return json_response("No token given.", 400)
