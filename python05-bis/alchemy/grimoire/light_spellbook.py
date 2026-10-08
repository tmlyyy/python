"""Record light spells using a deferred import to avoid a broken cycle."""


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Validate a light spell after both modules have been initialized."""
    from .light_validator import validate_ingredients

    validation: str = validate_ingredients(ingredients)
    status: str = "recorded" if validation.endswith(" - VALID") else "rejected"
    return f"Spell {status}: {spell_name} ({validation})"
