def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        data: dict = {}
        data["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")
    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 10
        open("missing.txt")
        data = {}
        data["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")
