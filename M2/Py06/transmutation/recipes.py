from Py06.alchemy.elements import create_air  # absolute import
from ..alchemy.potions import strength_potion  # relative import
from Py06.elements import create_fire  # root-level absolute import


def lead_to_gold() -> str:
    """Return transmutation recipe string."""
    air = create_air()
    strength = strength_potion()
    fire = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{strength}' mixed with '{fire}'"
    )
