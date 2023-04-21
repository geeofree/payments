from flask import Blueprint, session, request
from services.auth import AuthService
from utils.http import json_response

controller = Blueprint('users', __name__, url_prefix='/users')

@controller.route('/me')
def current_user():
    """
    /api/v1/users/me

    Response with the user claims from the decoded token.

    This controller assumes that the token will be validated before 
    it handles the request, therefore it assumes that the token is 
    always a valid token.
    """
    authorization = request.headers.get("authorization")
    token = authorization.split()[1]
    current_user = AuthService.decode_token(token)
    return json_response('Current user successfully retrieved.', data=current_user)
