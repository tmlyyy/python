"""Load laboratory configuration without exposing secret values."""

import os

from dotenv import load_dotenv


def main() -> None:
    """Prefer environment variables over the development .env file."""
    env_path: str = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(env_path, override=False)

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
    if mode == "development":
        print("Development: local service defaults are enabled.")
    else:
        print("Production: explicit service configuration is required.")
    database_status: str = (
        "Configured (value hidden)" if os.getenv("DATABASE_URL")
        else defaults["DATABASE_URL"] or "Missing"
    )
    api_status: str = (
        "Configured (value hidden)" if config["API_KEY"] else "Missing"
    )
    network_status: str = (
        "Configured (value hidden)" if os.getenv("ZION_ENDPOINT")
        else defaults["ZION_ENDPOINT"] or "Missing"
    )
    print(f"Database: {database_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Remote Network: {network_status}")

    print("\nConfiguration warnings:")
    missing: list[str] = [name for name in defaults if not os.getenv(name)]
    for name in missing:
        if config[name]:
            print(f"WARNING: {name} is unset or empty; using a default.")
        else:
            print(f"WARNING: {name} is unset or empty; configure it locally.")
    if not missing:
        print("All configuration variables are present.")


if __name__ == "__main__":
    main()
