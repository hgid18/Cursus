class Plant:

    def __init__(self, name: str, height: int, age: int):

        self.name: str = name
        self._age: int = age
        self.height: int = height

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self._age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")


rose = Plant("Rose", 30, 25)
i: int = 1
week: int = 7
print("=== Day 1 ===")
rose.get_info()
initial_height: int = rose.height
while i < week:
    rose.grow()
    rose.age()
    i += 1
print(f"=== Day {week} ===")
rose.get_info()
growth: int = rose.height - initial_height
print(f"Growth this week: +{growth}cm")
