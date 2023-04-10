from flask import Blueprint, session
from utils.http import json_response

controller = Blueprint('users', __name__, url_prefix='/users')

@controller.route('/me')
def current_user():
    return json_response('Current user successfully retrieved.', data=session['user'])
