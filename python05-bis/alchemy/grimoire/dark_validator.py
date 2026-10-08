"""Deliberately request a function from the partially initialized spellbook."""

from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    """Validate dark ingredients if the import cycle could finish."""
    for ingredient in dark_spell_allowed_ingredients():
        if ingredient in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
