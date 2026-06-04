import sys

print("=== Inventory System Analysis ===")

items: dict[str, int] = {}

for arg in sys.argv[1:]:
    parts: list[str] = arg.split(":")
    if len(parts) != 2 or parts[0] == "" or parts[1] == "":
        print(f"Error - invalid parameter '{arg}'")
        continue
    name: str = parts[0]
    if name in items:
        print(f"Redundant item '{name}' - discarding")
        continue
    try:
        quantity: int = int(parts[1])
        items[name] = quantity
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")

if len(items) == 0:
    print("Inventory is empty.")
    sys.exit()

print(f"Got inventory: {items}")
print(f"Item list: {list(items.keys())}")

total: int = sum(items.values())
print(f"Total quantity of the {len(items)} items: {total}")

for item, qty in items.items():
    pct: float = round((qty / total) * 100, 1)
    print(f"Item {item} represents {pct}%")

most: str = list(items.keys())[0]
least: str = list(items.keys())[0]
for item, qty in items.items():
    if qty > items[most]:
        most = item
    if qty < items[least]:
        least = item
print(f"Item most abundant: {most} with quantity {items[most]}")
print(f"Item least abundant: {least} with quantity {items[least]}")

items.update({'magic_item': 1})
print(f"Updated inventory: {items}")
