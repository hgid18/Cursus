class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, \
{self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, \
{self.trunk_diameter}cm diameter"

    def produce_shade(self):
        shade = self.height / 10
        print(f"{self.name} produces {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        return f"{self.name} (vegetable): {self.height}cm, \
{self.age} days, {self.harvest_season} harvest"


print("=== Garden Plant Types ===\n")

rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 20, 25, "yellow")

oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 300, 1460, 40)

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 60, 80, "autumn", "beta-carotene")

print(rose.get_info())
rose.bloom()
print(tulip.get_info())
tulip.bloom()
print("\n")

print(oak.get_info())
oak.produce_shade()
print(pine.get_info())
pine.produce_shade()
print("\n")

print(tomato.get_info())
tomato.nutrition()
print(carrot.get_info())
carrot.nutrition()