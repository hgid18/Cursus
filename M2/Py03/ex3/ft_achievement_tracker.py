def arch_hunter():
    print("=== Achievement Tracker System ===\n")

    archievement = set(['boss_slayer', 'collector',
                        'first_kill', 'level_10', 'perfectionist',
                        'speed_demon', 'treasure_hunter'])
    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['level_10', 'treasure_hunter', 'boss_slayer',
                   'speed_demon', 'perfectionist'])
    print(f"Player alice archievements: {alice}")
    print(f"Player bob archievements: {bob}")
    print(f"Player charlie archievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique archievements: {archievement}")
    print(f"Total unique archievements: {len(archievement)}\n")

    inter = alice.intersection(bob, charlie)
    bob_only = bob.difference(alice).difference(charlie)
    charlie_only = charlie.difference(alice).difference(bob)
    print(f"Common to all players: {inter}")
    print(f"Rare archievements (1 player): {bob_only}, {charlie_only}\n")

    albo = alice.intersection(bob)
    aluniq = alice.difference(bob)
    boluniq = bob.difference(alice)
    print(f"Alice vs bob common: {albo}")
    print(f"Alice unique: {aluniq}")
    print(f"Bob unique: {boluniq}")


arch_hunter()
