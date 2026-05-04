class Plant:

    def __init__(self, name: str, height: int, age: int):

        self.name: str = name
        self.age: int = age
        self.height: int = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    Plant1 = Plant("Rose", 25, 30)
    Plant2 = Plant("Sunflower", 80, 45)
    Plant3 = Plant("Cactus", 15, 120)

    Plant1.show()
    Plant2.show()
    Plant3.show()
