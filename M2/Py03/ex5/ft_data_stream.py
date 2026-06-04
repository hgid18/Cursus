import random
from typing import Generator

NAMES: list[str] = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS: list[str] = [
    'run', 'eat', 'sleep', 'grab', 'move',
    'climb', 'swim', 'use', 'release',
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(NAMES)
        action: str = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx: int = random.randint(0, len(events) - 1)
        event: tuple[str, str] = events[idx]
        events.pop(idx)
        yield event


print("=== Game Data Stream Processor ===")

stream: Generator[tuple[str, str], None, None] = gen_event()
for i in range(1000):
    name, action = next(stream)
    print(f"Event {i}: Player {name} did action {action}")

event_list: list[tuple[str, str]] = []
stream2: Generator[tuple[str, str], None, None] = gen_event()
for i in range(10):
    event_list.append(next(stream2))
print(f"\nBuilt list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
