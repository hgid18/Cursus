from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creature import Creature


def test_healing_factory() -> None:
    """Test healing Creature factory: describe, attack, heal."""
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform_factory() -> None:
    """Test transform Creature factory: describe, attack, transform, attack, revert."""
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    test_healing_factory()
    print()
    test_transform_factory()
