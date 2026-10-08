"""Demonstrate the package interface and an intentional missing attribute."""

import alchemy


def main() -> None:
    """Create air, then deliberately fail to access earth through alchemy."""
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    # Intentional AttributeError and mypy error required by the subject.
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")


if __name__ == "__main__":
    main()
