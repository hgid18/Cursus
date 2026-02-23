class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"

    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def get_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)\
, Prize points: {self.prize_points}"

    def get_type(self):
        return "prize"


class GardenManager:
    total_gardens = 0

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height):
        return height >= 0

    class GardenStats:
        @staticmethod
        def total_height(plants):
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def count_plant_types(plants):
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                plant_type = plant.get_type()
                if plant_type == "prize":
                    prize += 1
                elif plant_type == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def total_growth(plants):
            total = 0
            for plant in plants:
                total += (plant.height - plant.initial_height)
            return total

    def help_plants_grow(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def garden_info(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        total_growth = self.GardenStats.total_growth(self.plants)
        print(f"\nPlants added: {len(self.plants)}, \
Total growth: {total_growth}cm")
        regular, flowering, prize = \
            self.GardenStats.count_plant_types(self.plants)
        print(f"Plants types: {regular} regular, {flowering} flowering, \
{prize} prize flowers\n")

    def add_plant(self, plant):
        if not self.validate_height(plant.height):
            print(f"Invalid height for {plant.name}, rejected")
            return
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def calculate_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if plant.get_type() == "prize":
                score += plant.prize_points
            return score


oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

print("=== Garden Management System Demo ===\n")
alice_garden = GardenManager("Alice")
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)

alice_garden.help_plants_grow()
alice_garden.garden_info()

bob_garden = GardenManager("Bob")
bob_garden.add_plant(oak)
bob_garden.add_plant(rose)

bob_garden.help_plants_grow()
bob_garden.garden_info()

print(f"Height validation test: {GardenManager.validate_height(1)}")
print(f"Garden scores - Alice: {alice_garden.calculate_score()}, \
Bob: {bob_garden.calculate_score()}")
GardenManager.create_garden_network()