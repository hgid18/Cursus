import sys
import os
import site


def is_virtual_env() -> bool:
    """Return True if running inside a virtual environment."""
    return (
        hasattr(sys, "real_prefix")
        or (
            hasattr(sys, "base_prefix")
            and sys.base_prefix != sys.prefix
        )
    )


def get_venv_name() -> str:
    """Return the name of the current virtual environment."""
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    if venv_path:
        return os.path.basename(venv_path)
    return ""


def get_venv_path() -> str:
    """Return the full path of the current virtual environment."""
    return os.environ.get("VIRTUAL_ENV", "")


def get_site_packages() -> str:
    """Return the site-packages path for the current environment."""
    packages = site.getsitepackages()
    if packages:
        return packages[0]
    return "Not available"


def show_outside_venv() -> None:
    """Display information and instructions when outside a venv."""
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def show_inside_venv() -> None:
    """Display information when inside a virtual environment."""
    venv_name = get_venv_name()
    venv_path = get_venv_path()
    site_pkgs = get_site_packages()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site_pkgs)


def main() -> None:
    """Main entry point for the construct program."""
    if is_virtual_env():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
