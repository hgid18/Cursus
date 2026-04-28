import sys
import importlib.util
from typing import Optional


def check_package(name: str) -> Optional[str]:
    """Return version string if package is installed, else None."""
    spec = importlib.util.find_spec(name)
    if spec is None:
        return None
    try:
        mod = importlib.import_module(name)
        version = getattr(mod, "__version__", "unknown")
        return str(version)
    except Exception:
        return None


def show_dependency_manager_info() -> None:
    """Show the difference between pip and Poetry."""
    print()
    print("Dependency manager comparison:")
    print("  pip:")
    print("    - Uses requirements.txt to list packages")
    print("    - Install with: pip install -r requirements.txt")
    print("    - Does NOT lock transitive dependency versions by default")
    print("  Poetry:")
    print("    - Uses pyproject.toml to declare dependencies")
    print("    - Generates poetry.lock for fully reproducible installs")
    print("    - Install with: poetry install")
    print("    - Manages virtual environments automatically")


def check_all_dependencies() -> bool:
    """Check all required packages and print their status."""
    required = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    all_ok = True
    print("Checking dependencies:")
    for pkg, description in required.items():
        version = check_package(pkg)
        if version:
            print(f"[OK] {pkg} ({version}) - {description}")
        else:
            print(f"[MISSING] {pkg} - {description}")
            all_ok = False

    if not all_ok:
        print()
        print("Some dependencies are missing. Install them with:")
        print("  pip:    pip install -r requirements.txt")
        print("  Poetry: poetry install")
    return all_ok


def run_analysis() -> None:
    """Load Matrix data with numpy/pandas and visualize with matplotlib."""
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib  # type: ignore
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore

    print()
    print("Analyzing Matrix data...")
    n_points = 1000
    print(f"Processing {n_points} data points...")

    # Generate simulated Matrix data using numpy (required by subject)
    rng = np.random.default_rng(seed=42)
    time_steps = np.arange(n_points)
    signal = rng.normal(loc=0.0, scale=1.0, size=n_points)
    noise = rng.uniform(low=-0.5, high=0.5, size=n_points)
    matrix_data = signal + noise

    # Manipulate with pandas
    df = pd.DataFrame({
        "time": time_steps,
        "matrix_signal": matrix_data,
        "rolling_mean": pd.Series(matrix_data).rolling(window=50).mean(),
    })

    print("Generating visualization...")
    fig, axes = plt.subplots(2, 1, figsize=(12, 6))

    axes[0].plot(
        df["time"], df["matrix_signal"],
        color="green", alpha=0.6, linewidth=0.8, label="Matrix signal"
    )
    axes[0].plot(
        df["time"], df["rolling_mean"],
        color="red", linewidth=2, label="Rolling mean (50)"
    )
    axes[0].set_title("Matrix Data Stream")
    axes[0].set_xlabel("Time step")
    axes[0].set_ylabel("Signal amplitude")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].hist(
        df["matrix_signal"].dropna(),
        bins=40, color="green", alpha=0.7, edgecolor="black"
    )
    axes[1].set_title("Signal Distribution")
    axes[1].set_xlabel("Amplitude")
    axes[1].set_ylabel("Frequency")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    output_file = "matrix_analysis.png"
    plt.savefig(output_file, dpi=100)
    plt.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    """Main entry point for the loading program."""
    print("LOADING STATUS: Loading programs...")
    print()

    all_ok = check_all_dependencies()
    show_dependency_manager_info()

    if not all_ok:
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
