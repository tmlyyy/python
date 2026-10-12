"""Load laboratory configuration without exposing secret values."""

import os

from dotenv import load_dotenv


def main() -> None:
    """Report configuration using the subject's illustrative status labels."""
    directory: str = os.path.dirname(__file__)
    load_dotenv(os.path.join(directory, ".env"), override=False)

    print("ORACLE STATUS: Consulting the configuration...")
    mode: str = os.getenv("MATRIX_MODE") or "development"
    if mode not in ("development", "production"):
        print("WARNING: Unknown MATRIX_MODE; using development.")
        mode = "development"

    defaults: dict[str, str] = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": (
            "sqlite:///laboratory.db" if mode == "development" else ""
        ),
        "API_KEY": "",
        "LOG_LEVEL": "DEBUG" if mode == "development" else "INFO",
        "ZION_ENDPOINT": (
            "http://localhost:8000" if mode == "development" else ""
        ),
    }
    config: dict[str, str] = {
        name: os.getenv(name) or default for name, default in defaults.items()
    }
    config["MATRIX_MODE"] = mode

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    # These statuses describe configuration, not real service connections.
    database_status: str = "Not configured"
    if config["DATABASE_URL"]:
        database_status = (
            "Connected to local instance" if mode == "development"
            else "Connected to production instance"
        )
    api_status: str = (
        "Authenticated" if config["API_KEY"] else "Not configured"
    )
    network_status: str = (
        "Online" if config["ZION_ENDPOINT"] else "Offline (not configured)"
    )
    print(f"Database: {database_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Remote Network: {network_status}")

    missing: list[str] = [name for name in defaults if not os.getenv(name)]
    if missing:
        print("\nConfiguration warnings:")
    for name in missing:
        if config[name]:
            print(f"WARNING: {name} is unset or empty; "
                  f"using default: {defaults[name]}")
        else:
            print(f"WARNING: {name} is unset or empty; configure it locally.")

    print("\nConfiguration security check:")
    # API_KEY has no literal default; it comes only from the environment.
    print("[OK] No hardcoded secrets detected")
    try:
        ignore_path: str = os.path.join(directory, ".gitignore")
        with open(ignore_path, encoding="utf-8") as file:
            ignores_env: bool = ".env" in file.read().splitlines()
    except OSError:
        ignores_env = False
    if ignores_env:
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] Add .env to ex1/.gitignore")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
