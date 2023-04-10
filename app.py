from flask import Flask
import routes

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    routes.register(app)
    return app

app = create_app()
