"""Exercise 0: Lambda Sanctum.

Master anonymous functions and lambda expressions.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level descending."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages with power >= min_power."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add '* ' prefix and ' *' suffix to each spell name."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate max, min and average power of mages."""
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(
            sum(map(lambda m: m['power'], mages)) / len(mages), 2
        ),
    }


def main() -> None:
    """Demonstrate lambda expressions with artifacts, mages and spells."""
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Cloak', 'power': 70, 'type': 'armor'},
    ]

    mages = [
        {'name': 'Aria', 'power': 95, 'element': 'fire'},
        {'name': 'Brom', 'power': 45, 'element': 'earth'},
        {'name': 'Cela', 'power': 78, 'element': 'water'},
        {'name': 'Dorn', 'power': 30, 'element': 'wind'},
    ]

    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before "
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 70)
    print(f"Mages with power >= 70: {[m['name'] for m in strong_mages]}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
          f"Avg: {stats['avg_power']}")


if __name__ == "__main__":
    main()
