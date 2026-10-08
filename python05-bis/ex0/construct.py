"""Show whether the current Python interpreter uses a virtual environment."""

import os
import site
import sys


def show_package_paths(label: str, paths: list[str]) -> None:
    """Print the package directories for one Python installation."""
    print(f"{label}:")
    for path in paths:
        print(f"  {path}")


def main() -> None:
    """Describe the active interpreter and how its packages are isolated."""
    in_virtual_env: bool = sys.prefix != sys.base_prefix
    global_paths: list[str] = site.getsitepackages([sys.base_prefix])

    if in_virtual_env:
        print("LABORATORY STATUS: The laboratory is sealed")
    else:
        print("LABORATORY STATUS: You are working in the open")

    print(f"\nCurrent Python: {sys.executable}")

    if in_virtual_env:
        environment_name: str = os.path.basename(os.path.normpath(sys.prefix))
        print(f"Virtual Environment: {environment_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Packages installed here do not affect the global Python.")
        show_package_paths("Virtual environment package locations",
                           site.getsitepackages())
        show_package_paths("Global package locations", global_paths)
    else:
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Packages installed here may affect other projects.")
        show_package_paths("Global package locations", global_paths)
        print("A virtual environment uses its own package location.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate  # On Unix")
        print("lab_env\\Scripts\\activate  # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
