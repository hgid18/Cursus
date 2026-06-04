import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter new coordinates as floats in format"
                         " 'x,y,z': ")
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            bad: str = ""
            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    bad = part.strip()
                    break
            print(f"Error on parameter '{bad}': {e}")


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")
pos1: tuple[float, float, float] = get_player_pos()
x1: float
y1: float
z1: float
x1, y1, z1 = pos1
print(f"Got a first tuple: {pos1}")
print(f"It includes: X={x1}, Y={y1}, Z={z1}")
dist1: float = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
print(f"Distance to center: {round(dist1, 4)}")

print("\nGet a second set of coordinates")
pos2: tuple[float, float, float] = get_player_pos()
x2: float
y2: float
z2: float
x2, y2, z2 = pos2
dist2: float = math.sqrt(
    (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
)
print(f"Distance between the 2 sets of coordinates: {round(dist2, 4)}")
