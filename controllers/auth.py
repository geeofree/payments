from flask import Blueprint, request
from services.auth import AuthService
from middlewares.validation import ValidationMiddleware
from schemas.validation.auth import AuthValidationSchema
from utils.http import json_response

controller = Blueprint('auth', __name__)

@controller.route("sign-in", methods=['POST'])
@ValidationMiddleware.json_schema(AuthValidationSchema.sign_in_schema)
def sign_in():
    token = AuthService.create_token(request.json)

    if token == None:
        return json_response('Invalid credentials. Please try again.', 400)

    return json_response('Sign-in successful!', data=token)
