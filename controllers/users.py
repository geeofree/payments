from flask import Blueprint, session, request, g
from middlewares import AuthMiddleware
from services import UserService, AuthService
from utils.http import json_response

controller = Blueprint("users", __name__, url_prefix="/users")

@controller.route("/me")
def current_user():
    """
    :uri_path: /api/v1/users/me

    Endpoint for returning the current user from the JWT token.
    """
    return json_response("Current user successfully retrieved.", data=g.user)


@controller.route("/", methods=["POST"])
@AuthMiddleware.has_roles("master", "admin")
def create_user():
    """
    :uri_path: /api/v1/users

    Endpoint for creating subordinate users based on the current 
    user's role.
    """
    role = AuthService.get_subordinate_role()
    new_user = UserService.create_user(role=role, **request.json)
    return json_response("User successfully created.", status_code=201, data=new_user)
