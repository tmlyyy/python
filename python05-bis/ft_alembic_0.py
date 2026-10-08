"""Access the root elements module with an import statement."""

import elements


def main() -> None:
    """Create fire through the module interface."""
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
