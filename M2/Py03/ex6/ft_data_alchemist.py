import random

print("=== Game Data Alchemist ===")

players: list[str] = [
    'Alice', 'bob', 'Charlie', 'dylan',
    'Emma', 'Gregory', 'john', 'kevin', 'Liam',
]
print(f"Initial list of players: {players}")

all_capitalized: list[str] = [p.capitalize() for p in players]
print(f"New list with all names capitalized: {all_capitalized}")

only_capitalized: list[str] = [p for p in players if p[0].isupper()]
print(f"New list of capitalized names only: {only_capitalized}")

scores: dict[str, int] = {
    p: random.randint(0, 1000) for p in all_capitalized
}
print(f"Score dict: {scores}")

total: float = sum(scores.values())
average: float = round(total / len(scores), 2)
print(f"Score average is {average}")

high_scores: dict[str, int] = {
    p: s for p, s in scores.items() if s > average
}
print(f"High scores: {high_scores}")
