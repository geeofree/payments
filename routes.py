from flask import Blueprint
from middlewares.auth import validate_token
import controllers.auth as auth
import controllers.hello as hello

def register(app):
    """
    Registers and sets the different application routes.
    """
    api_auth = Blueprint('api_auth', __name__, url_prefix='/api/auth')
    api_auth.register_blueprint(auth.controller)

    api = Blueprint('api', __name__, url_prefix='/api/v1')
    api.before_request(validate_token)
    api.register_blueprint(hello.controller)

    app.register_blueprint(api_auth)
    app.register_blueprint(api)
