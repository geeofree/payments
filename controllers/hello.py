from flask import Blueprint
from utils.http import json_response

controller = Blueprint('hello', __name__)

@controller.route('/')
def index():
    return json_response('Hello world!')
