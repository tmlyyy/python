"""Validate light ingredients using the spellbook's allowed list."""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Accept text containing an allowed ingredient, ignoring case."""
    allowed: list[str] = light_spell_allowed_ingredients()
    valid: bool = any(item in ingredients.lower() for item in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
