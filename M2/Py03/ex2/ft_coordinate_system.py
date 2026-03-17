import math

position: tuple[int, int, int] = (10, 20, 5)
point1: tuple[int, int, int] = (0, 0, 0)
point2: tuple[int, int, int] = (10, 20, 5)

x1: int
y1: int
z1: int
x1, y1, z1 = point1
x2: int
y2: int
z2: int
x2, y2, z2 = point2
distance: float = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)
print("=== Game Coordinate System ===\n")
print(f"Position created: {position}")
print(f"Distance between {point1} and {point2}: {distance}")

coordinate: str = "3,4,0"
parse: list[str] = coordinate.split(",")
x: int = int(parse[0])
y: int = int(parse[1])
z: int = int(parse[2])
parsed_position: tuple[int, int, int] = (x, y, z)
print(f"\nParsing coordinates: {coordinate}")
print(f"Parsed position: {parsed_position}")

x1, y1, z1 = (0, 0, 0)
x2, y2, z2 = parsed_position
distance2: float = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)
print(f"Distance between {point1} and {parsed_position}: {distance2}")

invalid_cords: str = "abc,def,ghi"
print(f"\nParsing invalid cordinates: {invalid_cords}")
try:
    parse_cord: list[str] = invalid_cords.split(",")
    x = int(parse_cord[0])
    y = int(parse_cord[1])
    z = int(parse_cord[2])
    invalid_parsed: tuple[int, int, int] = (x, y, z)
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: ValueError, Args: {e.args}")

print("\nUnpacking demonstration:")
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
