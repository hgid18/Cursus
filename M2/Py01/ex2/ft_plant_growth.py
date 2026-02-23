class Plant:

    def __init__(self, name: str, height: int, age: int):

        self.name: str = name
        self.age: int = age
        self.height: int = height

    def grow(self):
        self.height += 1

    def time(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 30, 25)
i = 1
week = 7
print("=== Day 1 ===")
rose.get_info()
initial_height = rose.height
while i < week:
    rose.grow()
    rose.time()
    i += 1
print(f"=== Day {week} ===")
rose.get_info()
growth = rose.height - initial_height
print(f"Growth this week: +{growth}cm")
