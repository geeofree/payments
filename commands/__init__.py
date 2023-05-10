from .database import db_cli

def register(app):
    """
    Registers custom flask commands.
    """
    app.cli.add_command(db_cli)
