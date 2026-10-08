"""Deliberately import the validator before defining what it needs."""

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Describe a dark spell; the import cycle prevents reaching this call."""
    validation: str = dark_validate_ingredients(ingredients)
    if validation.endswith(" - INVALID"):
        return f"Spell rejected: {spell_name} ({validation})"
    return f"Spell recorded: {spell_name} ({validation})"
