class SecurePlant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: {age}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._age = age
            print(f"Age updated: {age}days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 25, 30)
SecurePlant("Rose", -25, -30)
print(f"Current Plant: {plant.name} ({plant.get_height()}cm, \
{plant.get_age()} days)")
