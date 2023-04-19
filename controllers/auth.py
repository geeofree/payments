from flask import Blueprint, request
from services.auth import AuthService
from utils.http import json_response

controller = Blueprint('auth', __name__)

@controller.route("sign-in", methods=['POST'])
def sign_in():
    token = AuthService.create_token(request.json)

    if token == None:
        return json_response('Invalid credentials. Please try again.', 400)

    return json_response('Sign-in successful!', data=token)
