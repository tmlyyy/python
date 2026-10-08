"""Trigger the intentional circular import in the dark grimoire."""


def main() -> None:
    """Import the dark spellbook directly and let its circular import fail."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(f"Testing record dark spell: {dark_spell_record('Night', 'bats')}")


if __name__ == "__main__":
    main()
