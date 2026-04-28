from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    """Create base and evolved Creature, describe and attack with each."""
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    """Make the base Creatures of two factories fight each other."""
    print("Testing battle")
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()
    print(creature_a.describe())
    print(" vs.")
    print(creature_b.describe())
    print(" fight!")
    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)
