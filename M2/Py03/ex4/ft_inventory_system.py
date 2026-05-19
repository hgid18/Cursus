import sys
print("=== Inventory System Analysis ===")
items = {}
for arg in sys.argv[1:]:
    parse = arg.split(":")
    item = parse[0]
    quantity = int(parse[1])
    items[item] = quantity
total_items = 0
for quantity in items.values():
    total_items += quantity
unique_type = len(items)
print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {unique_type}")

print("\n=== Current Inventory ===")
for item, quantity in items.items():
    percentage = (quantity / total_items) * 100
    print(f"{item}: {quantity} units ({percentage:.1f}%)")

print("\n=== Inventory Statistics ===")
top = 1
winner = ""
for name, size in items.items():
    if size > top:
        top = size
        winner = name
print(f"Most abundant: {winner} ({top} units)")
bot = 2
loser = ""
for name1, size1 in items.items():
    if size1 < bot:
        bot = size1
        loser = name1
print(f"Least abundant: {loser} ({bot} units)")

print("\n=== Item Categories ===")
moderate = {}
scarce = {}
for item, quantity in items.items():
    if quantity > 3:
        moderate[item] = quantity
    else:
        scarce[item] = quantity
print(f"Moderate: {moderate}")
print(f"Scarce: {scarce}")

print("\n=== Management Suggestions ===")
restock = []
for item, quantity in items.items():
    if quantity == 1:
        restock.append(item)
print(f"Restock needed: {restock}")

print("\n=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {list(items.keys())}")
print(f"Dictionary values: {list(items.values())}")
sword_exist = items.get('sword') is not None
print(f"Sample lookup - 'sword' in inventory: {sword_exist}")
