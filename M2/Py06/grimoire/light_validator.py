LIGHT_ALLOWED: list[str] = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    """Return VALID or INVALID based on light magic allowed ingredients."""
    lower = ingredients.lower()
    for allowed in LIGHT_ALLOWED:
        if allowed in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
