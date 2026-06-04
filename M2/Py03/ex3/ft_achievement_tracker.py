import random

ALL_ACHIEVEMENTS: list[str] = [
    'Boss Slayer', 'Collector Supreme', 'Crafting Genius',
    'First Steps', 'Hidden Path Finder', 'Master Explorer',
    'Perfectionist', 'Sharp Mind', 'Speed Runner', 'Strategist',
    'Survivor', 'Treasure Hunter', 'Untouchable', 'Unstoppable',
    'World Savior',
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(4, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


print("=== Achievement Tracker System ===")

players: dict[str, set[str]] = {
    'Alice': gen_player_achievements(),
    'Bob': gen_player_achievements(),
    'Charlie': gen_player_achievements(),
    'Dylan': gen_player_achievements(),
}

for name, achievements in players.items():
    print(f"Player {name}: {achievements}")

all_achievements: set[str] = set()
for achievements in players.values():
    all_achievements = all_achievements.union(achievements)

print(f"\nAll distinct achievements: {all_achievements}")

common: set[str] = set(ALL_ACHIEVEMENTS)
for achievements in players.values():
    common = common.intersection(achievements)
print(f"Common achievements: {common}")

print()
for name, achievements in players.items():
    others: set[str] = set()
    for other_name, other_ach in players.items():
        if other_name != name:
            others = others.union(other_ach)
    unique: set[str] = achievements.difference(others)
    print(f"Only {name} has: {unique}")

print()
for name, achievements in players.items():
    missing: set[str] = set(ALL_ACHIEVEMENTS).difference(achievements)
    print(f"{name} is missing: {missing}")
