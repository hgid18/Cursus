def garden_operations(operation_number: int) -> None:

    if (operation_number == 0):
        print("Testing operation 0...")
        int("abc")
    elif (operation_number == 1):
        print("Testing operation 1...")
        10 / 0
    elif (operation_number == 2):
        print("Testing operation 2...")
        open("/non/existent/file")
    elif (operation_number == 3):
        print("Testing operation 3...")
        "hola" + 1
    else:
        print("Testing operation 4...")
        print("Operation completed successfully\n")


def test_error_types() -> None:
    for i in range(5):
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


print("=== Garden Error Types Demo ===")
test_error_types()
print("All error types tested successfully!")
