"""Import potion functions directly from their module."""

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    """Brew both potions."""
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
