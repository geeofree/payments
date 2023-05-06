from flask import Blueprint, session, request
from services import AuthService
from utils.http import json_response

controller = Blueprint('users', __name__, url_prefix='/users')

@controller.route('/me')
def current_user():
    """
    :uri_path: /api/v1/users/me

    Endpoint for returning the current user from the JWT token.

    This controller assumes that the token will be validated before 
    it handles the request; it assumes that the JWT token is 
    always valid.
    """
    authorization = request.headers.get("authorization")
    token = authorization.split()[1]
    current_user = AuthService.decode_token(token)
    return json_response('Current user successfully retrieved.', data=current_user)
