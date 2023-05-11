from alembic.config import Config as AlembicConfig
import alembic.command as alembic_command
from app_setup import create_app
from dotenv import load_dotenv
import pytest

load_dotenv()

_in_memory_db = "sqlite:///test.db"
_alembic_config = AlembicConfig("alembic.ini")
_alembic_config.set_main_option("sqlalchemy.url", _in_memory_db)

@pytest.fixture
def db_connection():
    alembic_command.upgrade(_alembic_config, "head")
    yield _in_memory_db
    alembic_command.downgrade(_alembic_config, "base")

@pytest.fixture
def app(db_connection):
    app = create_app(db_connection=db_connection)
    return app

@pytest.fixture
def client(app):
    return app.test_client()
