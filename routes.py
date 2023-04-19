from flask import Blueprint
from middlewares.auth import AuthMiddleware
import controllers.auth as auth
import controllers.users as users

def register(app):
    """
    Registers and sets the different application routes.
    """
    # API/Auth Blueprints
    api_auth = Blueprint('api_auth', __name__, url_prefix='/api/auth')
    api_auth.register_blueprint(auth.controller)

    # API/v1 Blueprints
    api = Blueprint('api', __name__, url_prefix='/api/v1')

    # Middlewares
    api.before_request(AuthMiddleware.validate_token)

    # Controllers
    api.register_blueprint(users.controller)

    # Register top level blueprints
    app.register_blueprint(api_auth)
    app.register_blueprint(api)
