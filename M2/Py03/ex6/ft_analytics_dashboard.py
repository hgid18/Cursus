print("=== Game Analytics Dashboard ===")

players = ["alice", "bob", "charlie", "diana"]
archievements = {"first_kill", "level_10", "boss_slayer"}
players_archievements = {"alice": 5, "bob": 3, "charlie": 7, "diana": 4}
players_scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 2050}
regions = {"north", "east", "central"}
total_players = len(players)
total_archievements = len(archievements)

score = 0
for name in players_scores:
    score += players_scores[name]
total_score = sum([players_scores[name] for name in players_scores])
average_score = total_score / len(players)
top_performer = "alice (2300 points, 5 archievements)"
high_scorer = [name for name in players_scores if players_scores[name] > 2000]
scores_doubled = [players_scores[name] * 2 for name in players_scores]
active_players = [name for name in players_archievements if
                  players_archievements[name] > 3]

print("\n=== List Comprehension Examples ===")
print(f"High scorers (>2000): [{high_scorer}]")
print(f"Cores doubled: {scores_doubled}")
print(f"Active players: {active_players}")

high_count = len([name for name in players_scores if players_scores[name] >
                  2000])
medium_count = len([name for name in players_scores if 1500
                    <= players_scores[name] <= 2000])
low_count = len([name for name in players_scores if players_scores[name] <
                1500])

print("\n=== Dict Comprehension Examples ===")
print(f"Player scores: {players_scores}")
print(f"Score categories: {high_count}, {medium_count}, {low_count}")
print(f"Archievements counts: {players_archievements}")

print("\n=== Set Comprehension Examples ===")
print(f"Unique players: {players}")
print(f"Unique archievements: {archievements}")
print(f"Active regions: {regions}")

print("\n=== Combined Analysis ===")
print(f"Total players: {total_players}")
print(f"Total unique archievements: {total_archievements}")
print(f"Average score: {average_score}")
print(f"Top performe: {top_performer}")
