class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if not plant_name or not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


print("=== Garden Watering System ===\n")
print("Testing valid plants...")


def test_watering_system() -> None:
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")
    try:
        print("Testing invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print(".. ending tests and returning to main")


test_watering_system()
print("Closing watering system\n")
print("Cleanup always happens, even with errors!")
