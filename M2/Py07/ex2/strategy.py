from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    """Abstract strategy defining how a Creature acts in battle."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if this strategy is suitable for the given Creature."""
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Execute the strategy for the given Creature."""
        ...


class NormalStrategy(BattleStrategy):
    """Strategy suitable for any Creature: just attack."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy suitable for TransformCapability Creatures: transform, attack, revert."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        transform_creature = creature  # type: ignore[assignment]
        print(transform_creature.transform())  # type: ignore[attr-defined]
        print(creature.attack())
        print(transform_creature.revert())  # type: ignore[attr-defined]


class DefensiveStrategy(BattleStrategy):
    """Strategy suitable for HealCapability Creatures: attack then heal."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        heal_creature = creature  # type: ignore[assignment]
        print(heal_creature.heal())  # type: ignore[attr-defined]
