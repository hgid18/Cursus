class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age
        self._statistics: Plant.Statistics = Plant.Statistics()

    def grow(self) -> None:
        self._height += 1
        self._statistics.grow_count += 1

    def age(self) -> None:
        self._age += 1
        self._statistics.age_count += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._statistics.show_count += 1

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def get_statistics(self) -> "Plant.Statistics":
        return self._statistics

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class Statistics:
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, \
{self.show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True
        print(f"{self._name} is blooming beautifully!")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
        self._statistics.show_count += 1


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._statistics: Tree.Statistics = Tree.Statistics()

    def produce_shade(self) -> None:
        shade_length: float = float(self._height)
        shade_width: float = self._trunk_diameter
        print(f"Tree {self._name} now produces a shade of {shade_length}cm \
long and {shade_width}cm wide.")
        self._statistics.produce_shade_count += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Trunk diameter: {self._trunk_diameter}cm")
        self._statistics.show_count += 1

    def get_statistics(self) -> "Tree.Statistics":
        return self._statistics

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self.produce_shade_count: int = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, \
{self.show_count} show")
            print(f"{self.produce_shade_count} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def grow(self) -> None:
        self._height += 2
        self._nutritional_value += 1
        self._statistics.grow_count += 1

    def age(self) -> None:
        self._age += 1
        self._nutritional_value += 1
        self._statistics.age_count += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")
        self._statistics.show_count += 1


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str,
                 seeds: int = 0) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = seeds

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
        print(f"Seeds: {self._seeds}")
        self._statistics.show_count += 1


def display_stats(plant: Plant) -> None:
    plant.get_statistics().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymous)
