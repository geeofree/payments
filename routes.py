from flask import Blueprint
import controllers.hello as hello

def register(app):
    """
    Registers and sets the different application routes.
    """
    api = Blueprint('api', __name__, url_prefix='/api')

    api.register_blueprint(hello.controller)

    app.register_blueprint(api)
