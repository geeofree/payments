from flask import Blueprint

controller = Blueprint('hello', __name__)

@controller.route('/')
def index():
    return '<h1>Hello world!</h1>'
