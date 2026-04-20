class Plant:

    def __init__(self, name: str, height: int, age: int):

        self.name: str = name
        self.age: int = age
        self.height: int = height

    def get_info(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


print("=== Plant Factory Output ===")
list_plants = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

plants: list[Plant] = []

for data in list_plants:
    plant: Plant = Plant(data[0], data[1], data[2])
    plants.append(plant)
    plant.get_info()

print("\nTotal plants created: 5")
