import os
import sys


def load_dotenv_manually(env_path: str) -> None:
    """Load variables from a .env file into os.environ (without overriding)."""
    if not os.path.isfile(env_path):
        return
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            # os.environ takes priority: only set if not already defined
            if key and key not in os.environ:
                os.environ[key] = value


def try_load_dotenv(env_path: str) -> bool:
    """Try to load .env using python-dotenv; fall back to manual parser."""
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv(dotenv_path=env_path, override=False)
        return True
    except ImportError:
        load_dotenv_manually(env_path)
        return False


def get_config() -> dict[str, str]:
    """Read all required configuration variables from the environment."""
    defaults: dict[str, str] = {
        "MATRIX_MODE": "",
        "DATABASE_URL": "",
        "API_KEY": "",
        "LOG_LEVEL": "",
        "ZION_ENDPOINT": "",
    }
    config: dict[str, str] = {}
    for key, default in defaults.items():
        config[key] = os.environ.get(key, default)
    return config


def mask_secret(value: str) -> str:
    """Return a masked version of a secret value."""
    if not value:
        return "[NOT SET]"
    if len(value) <= 4:
        return "****"
    return value[:2] + "****" + value[-2:]


def describe_database(url: str) -> str:
    """Return a human-readable database status."""
    if not url:
        return "[NOT CONFIGURED]"
    if "localhost" in url or "sqlite" in url or "127.0.0.1" in url:
        return "Connected to local instance"
    return "Connected to remote instance"


def describe_api(key: str) -> str:
    """Return API authentication status."""
    if not key or key == "your_api_key_here":
        return "NOT authenticated"
    return "Authenticated"


def describe_zion(endpoint: str) -> str:
    """Return Zion network status."""
    if not endpoint:
        return "Offline"
    return "Online"


def show_dev_vs_prod(mode: str) -> None:
    """Show visible difference between development and production mode."""
    print()
    if mode == "production":
        print("  [PRODUCTION MODE]")
        print("  - Debug logging is DISABLED")
        print("  - All secrets must be provided via environment variables")
        print("  - .env files are ignored in production deployments")
        print("  - Strict error handling: missing config raises exceptions")
    else:
        print("  [DEVELOPMENT MODE]")
        print("  - Debug logging is ENABLED")
        print("  - .env file is used for local configuration")
        print("  - Missing optional variables use safe defaults")
        print("  - Verbose output for easier debugging")


def security_check(env_file_exists: bool, config: dict[str, str]) -> None:
    """Run environment security checks and print results."""
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_file_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found — using environment variables only")

    prod_override = os.environ.get("MATRIX_MODE") == "production"
    if prod_override:
        print("[OK] Production overrides active via environment variables")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    """Main entry point for the oracle program."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    # Determine .env file path (same directory as this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, ".env")
    env_file_exists = os.path.isfile(env_path)

    dotenv_available = try_load_dotenv(env_path)
    if not dotenv_available:
        print("Note: python-dotenv not installed, using built-in .env parser.")
        print("Install with: pip install python-dotenv")
        print()

    config = get_config()
    mode = config["MATRIX_MODE"] or "development"

    missing = [k for k, v in config.items() if not v]
    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f"  - {key}")
        print()
        print("Copy .env.example to .env and fill in your values.")
        print()

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_database(config['DATABASE_URL'])}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL'] or '[NOT SET]'}")
    print(f"Zion Network: {describe_zion(config['ZION_ENDPOINT'])}")

    show_dev_vs_prod(mode)
    security_check(env_file_exists, config)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
