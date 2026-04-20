class SecurePlant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = 0
        self._age: int = 0
        self._height = height
        self._age = age
        print(f"Plant created: {self._name}: {height}cm, {age} days old")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 15, 10)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.set_age(-10)
    print(f"Current state: {plant.get_name()}: {plant.get_height()}cm, {plant.get_age()} days old")
