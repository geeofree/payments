from flask import Blueprint, request
from services import AuthService, UserService
from middlewares import ValidationMiddleware
from schemas.validation import AuthValidationSchema
from utils.http import json_response

controller = Blueprint('auth', __name__)

@controller.route("sign-in", methods=['POST'])
@ValidationMiddleware.json_schema(AuthValidationSchema.sign_in_schema)
def sign_in():
    """
    :uri_path: /api/auth/sign-in

    Endpoint for signing-in users.

    :return: The JWT token if the sign-in was successful, an error JSON
             response otherwise.
    """
    token = AuthService.create_token(request.json)

    if token == None:
        return json_response('Invalid credentials. Please try again.', 400)

    return json_response('Sign-in successful!', data=token)


@controller.route("sign-up", methods=['POST'])
@ValidationMiddleware.json_schema(AuthValidationSchema.sign_up_schema)
def sign_up():
    """
    :uri_path: /api/auth/sign-up

    Endpoint for signing-up client users.

    :return: The newly created user.
    """
    new_user = UserService.create_user(**request.json)
    return json_response("Sign-up successful!", status_code=201, data=new_user)
