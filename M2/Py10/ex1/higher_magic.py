"""Exercise 1: Higher Realm.

Discover the power of higher-order functions.
"""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a new function that calls both spells and returns a tuple."""
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell where power is multiplied before casting."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts if the condition is True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells in order."""
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    """Demonstrate higher-order functions with spell modifiers."""
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} armor"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Troll", 10)
    amplified = mega_fireball("Troll", 10)
    print(f"Original: {original}")
    print(f"Amplified: {amplified}")

    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(
        lambda t, p: p >= 50,
        fireball
    )
    print(high_power_only("Goblin", 30))
    print(high_power_only("Dragon", 80))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Hero", 25)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
