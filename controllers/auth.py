from flask import Blueprint, request
import services.auth as auth_service
from utils.http import json_response

controller = Blueprint('auth', __name__)

@controller.route("sign-in")
def sign_in():
    token = auth_service.create_token(request.json)

    if token == None:
        return json_response('Invalid credentials. Please try again.', 400)

    return json_response('Sign-in successful!', token)
