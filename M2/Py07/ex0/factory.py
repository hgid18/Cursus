from abc import ABC, abstractmethod
from ex0.creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating Creature families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base Creature of the family."""
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved Creature of the family."""
        ...


class FlameFactory(CreatureFactory):
    """Factory for fire-type Creatures."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for water-type Creatures."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
