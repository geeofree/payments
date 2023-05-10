from flask import Flask
from database import db
import commands
import routes

def create_app(db_connection=None):
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_engine(
        db_connection or app.config.get("DB_CONNECTION"),
        echo=app.config.get('RUN_FROM_CLI') or app.config.get('DEBUG')
    )
    commands.register(app)
    routes.register(app)
    return app
