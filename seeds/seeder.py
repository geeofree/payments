class Seeder:
    _seeders = []

    def __init_subclass__(cls):
        Seeder._seeders.append(cls)


    @staticmethod
    def seed_up():
        for seeder in Seeder._seeders:
            print(f"=== {seeder.__name__}:seed_up ===")
            seeder.seed_up()


    @staticmethod
    def seed_down():
        for seeder in Seeder._seeders:
            print(f"=== {seeder.__name__}:seed_down ===")
            seeder.seed_down()