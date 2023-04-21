from flask import Flask
from database import db
import routes

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_engine(app.config.get("DB_CONNECTION"))
    routes.register(app)
    return app
