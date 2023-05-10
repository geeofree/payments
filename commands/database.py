from utils.exceptions import EmptyPackagesException
from flask.cli import AppGroup
from flask import current_app
from importlib import import_module
from datetime import datetime, timezone
import click
import os

db_cli = AppGroup('db')

_SEEDERS_DIRNAME = "seeds"

@db_cli.command('seed')
@click.argument('seeder_name')
def seed(seeder_name):
    seeds_dir = os.path.join(current_app.root_path, _SEEDERS_DIRNAME)

    if not os.path.exists(seeds_dir):
        os.makedirs(seeds_dir)
        print("Generated missing seeds directory: {}".format(seeds_dir))
        seeds_dir_init_file = os.path.join(seeds_dir, "__init__.py")
        with open(seeds_dir_init_file, 'w') as file:
            file.write("")
            print("Generated __init__ file for seeds directory: {}".format(seeds_dir_init_file))

    unix_ts = str(datetime.now(timezone.utc).timestamp()).replace('.', '_')
    seed_file = os.path.join(seeds_dir, "{}_{}.py".format(unix_ts, seeder_name))

    if os.path.exists(seed_file):
        raise FileExistsError("Seed file already exists: {}".format(seed_file))

    with open(seed_file, 'w') as file:
        file.write((
            "from database import db\n\n"
            "def seed_up():\n"
            "   with db.session as session:\n"
            "       pass\n\n\n"
            "def seed_down():\n"
            "   with db.session as session:\n"
            "       pass"
        ))
        print("Generated seeder file: {}".format(seed_file))


def _get_seeders():
    seeds_dir = os.path.join(current_app.root_path, _SEEDERS_DIRNAME)

    if not os.path.exists(seeds_dir):
        raise FileNotFoundError("Seeds directory not found: {}".format(seeds_dir))

    seeders = os.listdir(seeds_dir)
    seeders = filter(
        lambda seeder_file: (
            seeder_file != "__init__.py" and 
            os.path.isfile(os.path.join(seeds_dir, seeder_file))
        ),
        seeders
    )
    seeders = list(map(lambda seeder_file: "{}.{}".format(_SEEDERS_DIRNAME, seeder_file.replace(".py", '')), seeders))

    if len(seeders) == 0:
        raise EmptyPackagesException("No seeder files found.")

    return seeders


@db_cli.command('seed:up')
def seed_up():
    seeders = _get_seeders()
    for seeder in seeders:
        import_module(seeder).seed_up()


@db_cli.command('seed:down')
def seed_down():
    seeders = _get_seeders()
    for seeder in seeders:
        import_module(seeder).seed_down()
