"""Combine absolute and relative imports in a nested package."""

from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Describe the recipe that transmutes lead into gold."""
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' mixed with '{create_fire()}'")
