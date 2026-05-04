class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 1

    def age_method(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Color: {self.color}")

    def get_info(self) -> str:
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, \
{self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade: float = self.height / 10
        print(f"{self.name} produces {shade} square meters of shade")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def get_info(self) -> str:
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, \
{self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Harvest season: {self.harvest_season}")

    def get_info(self) -> str:
        return f"{self.name} (vegetable): {self.height}cm, \
{self.age} days, {self.harvest_season} harvest"


if __name__ == "__main__":
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
