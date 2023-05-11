from utils.exceptions import EmptyPackagesException
from flask.cli import AppGroup
from flask import current_app
from importlib import import_module
import click
import os

db_cli = AppGroup('db')

_SEEDERS_DIRNAME = "seeds"

@db_cli.command('seed')
@click.argument('seeder_name')
def seed(seeder_name):
    seeds_dir = os.path.join(current_app.root_path, _SEEDERS_DIRNAME)
    seeds_dir_init_file = os.path.join(seeds_dir, "__init__.py")

    if not os.path.exists(seeds_dir):
        os.makedirs(seeds_dir)
        print("Generated missing seeds directory: {}".format(seeds_dir))
        seeds_dir_seeder_file = os.path.join(seeds_dir, "seeder.py")
        with open(seeds_dir_seeder_file, 'w') as file:
            file.write(
                "class Seeder:\n"
                "    _seeders = []\n\n"
                "    def __init_subclass__(cls):\n"
                "        Seeder._seeders.append(cls)\n\n\n"
                "    @staticmethod\n"
                "    def seed_up():\n"
                "        for seeder in Seeder._seeders:\n"
                "            print(f\"=== {seeder.__name__}:seed_up ===\")\n"
                "            seeder.seed_up()\n\n\n"
                "    @staticmethod\n"
                "    def seed_down():\n"
                "        for seeder in Seeder._seeders:\n"
                "            print(f\"=== {seeder.__name__}:seed_down ===\")\n"
                "            seeder.seed_down()"
            )
            print("Generated seeder file for seeds directory: {}".format(seeds_dir_seeder_file))
        with open(seeds_dir_init_file, 'w') as file:
            file.write("from .seeder import Seeder\n")
            print("Generated __init__ file for seeds directory: {}".format(seeds_dir_init_file))

    seed_file = os.path.join(seeds_dir, f"{seeder_name}.py")

    if os.path.exists(seed_file):
        raise FileExistsError("Seed file already exists: {}".format(seed_file))

    seeder_cls_name = map(lambda s: s[0].upper() + s[1:], seeder_name.split('_'))
    seeder_cls_name = "".join(list(seeder_cls_name))
    seeder_cls_name = f"{seeder_cls_name}Seeder"

    with open(seed_file, 'w') as file:
        file.write(
            "from .seeder import Seeder\n\n"
            f"class {seeder_cls_name}(Seeder):\n"
            "    @staticmethod\n"
            "    def seed_up():\n"
            "        pass\n\n\n"
            "    @staticmethod\n"
            "    def seed_down():\n"
            "        pass"
        )
        print("Generated seeder file: {}".format(seed_file))

    with open(seeds_dir_init_file, 'a') as file:
        file.write(f"from .{seeder_name} import {seeder_cls_name}\n")


@db_cli.command('seed:up')
def seed_up():
    seeder = import_module("seeds").Seeder
    seeder.seed_up()


@db_cli.command('seed:down')
def seed_down():
    seeder = import_module("seeds").Seeder
    seeder.seed_down()
