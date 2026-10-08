"""Record a light spell through the grimoire package interface."""

import alchemy.grimoire


def main() -> None:
    """Demonstrate the working mutual dependency."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result: str = alchemy.grimoire.light_spell_record(
        "Fantasy", "Earth, wind and fire"
    )
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
