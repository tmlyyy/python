"""Check the external libraries declared for the laboratory."""

import importlib


def main() -> None:
    """Report installed versions and how to install missing libraries."""
    reagents: tuple[tuple[str, str], ...] = (
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
    )
    missing: bool = False

    print("REAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:")
    for name, purpose in reagents:
        try:
            module = importlib.import_module(name)
        except ImportError as error:
            missing = True
            print(f"[MISSING] {name}: {error}")
        else:
            version: str = str(getattr(module, "__version__", "unknown"))
            print(f"[OK] {name} ({version}) - {purpose}")

    if missing:
        print("\nInstall the missing reagents with either command:")
        print("pip install -r ex0/requirements.txt")
        print("poetry install  # Run from ex0/")

    print("\npip vs Poetry:")
    print("  requirements.txt lists constraints;")
    print("  pip resolves them at install time.")
    print("  pyproject.toml lists constraints; Poetry records exact resolved")
    print("  versions in poetry.lock when you run poetry install.")

    if not missing:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
