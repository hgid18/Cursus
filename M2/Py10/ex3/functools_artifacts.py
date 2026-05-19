"""Exercise 3: Ancient Library.

Explore the functools module's treasures.
"""

import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the specified operation."""
    if not spells:
        return 0

    ops: dict[str, Callable] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create 3 specialized enchantment functions using functools.partial."""
    return {
        'fire': functools.partial(base_enchantment, power=50, element='fire'),
        'ice': functools.partial(base_enchantment, power=50, element='ice'),
        'lightning': functools.partial(
            base_enchantment, power=50, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using lru_cache memoization."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single-dispatch spell system using functools.singledispatch."""
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    """Demonstrate functools: reduce, partial, lru_cache, singledispatch."""
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(target: str, power: int, element: str) -> str:
        return (
            f"{element.capitalize()} enchantment on {target} (power {power})"
        )

    enchants = partial_enchanter(base_enchant)
    print(enchants['fire']('Sword'))
    print(enchants['ice']('Shield'))
    print(enchants['lightning']('Bow'))

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["bolt", "flame", "frost"]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
