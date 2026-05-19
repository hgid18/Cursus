"""Exercise 4: Master's Tower.

Create powerful decorators and class methods.
"""

import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates the first argument as a power level."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if power >= min_power:
                return func(power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a spell up to max_attempts times."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """A guild that manages mages and their spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is at least 3 chars and only letters/spaces."""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient (min 10 required)."""
        if power >= 10:
            return f"Successfully cast {spell_name} with {power} power"
        return "Insufficient power for this spell"


def main() -> None:
    """Demonstrate decorators: spell_timer, power_validator, retry_spell."""
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(min_power=20)
    def thunder_strike(power: int, target: str) -> str:
        return f"Thunder strikes {target} for {power} damage"

    print(thunder_strike(10, "Goblin"))
    print(thunder_strike(50, "Dragon"))

    print("\nTesting retrying spell...")

    attempt_count = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 4:
            raise RuntimeError("Spell unstable")
        return "Stable!"

    print(unstable_spell())

    attempt_count[0] = 0

    @retry_spell(max_attempts=3)
    def always_succeeds() -> str:
        return "Waaaaaaagh spelled !"

    print(always_succeeds())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
