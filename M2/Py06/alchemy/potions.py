from Py06.alchemy.elements import create_earth, create_air
from Py06.alchemy.elements import create_fire, create_water


def healing_potion() -> str:
    """Return healing potion string using earth and air."""
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    """Return strength potion string using fire and water."""
    fire = create_fire()
    water = create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
