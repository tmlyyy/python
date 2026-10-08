"""Brew potions using elements from both sides of the package boundary."""

from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a healing potion with earth and air."""
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")


def strength_potion() -> str:
    """Brew a strength potion with fire and water."""
    return (f"Strength potion brewed with '{create_fire()}' "
            f"and '{create_water()}'")
