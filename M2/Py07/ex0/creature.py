from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all Creature cards."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    def describe(self) -> str:
        """Return a standard description of the Creature."""
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """Return a string describing the Creature's attack."""
        ...


class Flameling(Creature):
    """Base fire Creature."""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Evolved fire Creature."""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Base water Creature."""

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Evolved water Creature."""

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
