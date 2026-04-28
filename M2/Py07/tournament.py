from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """Run all pairwise battles between opponents using their strategies."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print()
            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # Tournament 0: basic (Flameling+Normal vs Healing+Defensive)
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print()

    # Tournament 1: error (Flameling+Aggressive vs Healing+Defensive)
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print()

    # Tournament 2: multiple (Aquabub+Normal, Healing+Defensive, Transform+Aggressive)
    print("Tournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])
