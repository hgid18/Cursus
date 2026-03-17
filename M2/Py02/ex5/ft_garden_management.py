from typing import Dict


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: Dict[str, Dict[str, int]] = {}

    def add_plant(self, name: str) -> None:
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": 5, "sun": 8}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                print(f"watering {plant} - success")
        except WaterError as e:
            print(f"Error while watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        print("\nChecking plant health...")
        for plant, data in self.plants.items():
            try:
                water: int = data["water"]
                sun: int = data["sun"]
                if water > 10:
                    raise PlantError(f"Water level {water} \
is too high (max 10)")
                print(f"{plant}: healthy (water: {water}, sun: {sun})")
            except PlantError as e:
                print(f"Error checking {plant}: {e}")

    def simulate_error(self) -> None:
        raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager: GardenManager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants()

    manager.plants["lettuce"]["water"] = 15
    manager.check_health()
    print("\nTesting error recovery...")
    try:
        manager.simulate_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
