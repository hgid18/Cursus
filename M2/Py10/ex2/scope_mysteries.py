"""Exercise 2: Memory Depths.

Understand lexical scoping and closures.
"""

from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a closure that counts how many times it has been called."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a closure that accumulates power starting from initial_power."""
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies the given enchantment to an item."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a dict with 'store' and 'recall' closures sharing storage."""
    vault: dict = {}

    def store(key: str, value: object) -> None:
        vault[key] = value

    def recall(key: str) -> object:
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    """Demonstrate closures and lexical scoping."""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    mv = memory_vault()
    mv['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {mv['recall']('secret')}")
    print(f"Recall 'unknown': {mv['recall']('unknown')}")


if __name__ == "__main__":
    main()
