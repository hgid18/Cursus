class Plant:

    def __init__(self, name: str, height: int, age: int):

        self.name: str = name
        self.age: int = age
        self.height: int = height

    def get_info(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


print("=== Plant Factory Output ===")
plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
    ]
print("=== Plant Factory Output ===")
for i in plants:
    i.get_info()

print("\nTotal plants created: 5")
