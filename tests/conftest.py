from alembic.config import Config as AlembicConfig
import alembic.command as alembic_command
from app_setup import create_app
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.fixture
def app():
    in_memory_db = "sqlite:///test.db"
    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", in_memory_db)

    app = create_app(db_connection=in_memory_db)

    @app.teardown_appcontext
    def db_teardown(exception):
        alembic_command.downgrade(alembic_config, "base")

    alembic_command.upgrade(alembic_config, "head")
    return app

@pytest.fixture
def client(app):
    return app.test_client()
