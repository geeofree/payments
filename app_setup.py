from flask import Flask
from database import db
import routes

def create_app(db_connection=None):
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_engine(db_connection or app.config.get("DB_CONNECTION"))
    routes.register(app)
    return app
