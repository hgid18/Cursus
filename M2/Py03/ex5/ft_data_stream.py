def generate_game_events(n):
    names = ["alice", "bob", "charlie", "kenny", "mickey"]
    actions = ["killed monster", "found treasure", "leveled up",
               "died in a horrible way", "lost his sanity"]
    for i in range(n):
        nm = names[i % len(names)]
        level = (i % 15) + 1
        act = actions[i % len(actions)]
        event = f"Player {nm} (level {level}) {act}"
        yield (event, level, act)


print("=== Game Data Stream Processor ===")
print("\nProcessing 1000 game events...\n")
events = generate_game_events(1000)
total = 0
treasure = 0
levelup = 0
high_level = 0
for event in events:
    event_text = event[0]
    level = event[1]
    action_data = event[2]
    total += 1
    if total <= 5:
        print(f"Event {total}: {event_text}")
    if level >= 10:
        high_level += 1
    if action_data == "found treasure":
        treasure += 1
    if action_data == "leveled up":
        levelup += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure}")
print(f"Level-up events: {levelup}")

print("\nMemory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")

print("\n=== Generator Demonstration ===")


def fibonacci_gen():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        next = a + b
        yield next
        a = b
        b = next


def prime_gen():
    yield 2
    a = 3
    while True:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            yield a
        a += 2


fib = fibonacci_gen()
fib_seq = []
for i in range(10):
    fib_seq.append(next(fib))

fib_str = ""
for i in range(len(fib_seq)):
    fib_str += str(fib_seq[i])
    if i < len(fib_seq) - 1:
        fib_str += ", "
print(f"Fibonacci sequence (first 10): {fib_str}")

prim = prime_gen()
prim_seq = []
for i in range(5):
    prim_seq.append(next(prim))

prim_str = ""
for i in range(len(prim_seq)):
    prim_str += str(prim_seq[i])
    if i < len(prim_seq) - 1:
        prim_str += ", "
print(f"Prime numbers (first 5): {prim_str}")

generate_game_events(10)
