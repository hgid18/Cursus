from typing import Union


def secure_archive(
    filename: str,
    action: Union[int, str] = "read",
    content: str = ""
) -> tuple[bool, str]:
    """
    Provides safe access to any file for reading or writing.
    Uses context manager (with statement) to ensure proper file handling.

    Args:
        filename: The name of the file to access (mandatory)
        action: The action to perform - "read" or 1 for read, "write" or 2 for write
        content: The content to write to the file (only used for write action)

    Returns:
        A tuple (success: bool, message: str) where success indicates if the
        operation succeeded and message contains either the file contents or
        an error message.
    """
    # Normalize action to string
    if isinstance(action, int):
        action = "read" if action == 1 else "write"

    try:
        if action == "read" or action == 1:
            with open(filename, 'r') as file:
                file_content: str = file.read()
            return (True, file_content)
        elif action == "write" or action == 2:
            with open(filename, 'w') as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: {action}")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    # Test 1: Read from nonexistent file
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file")
    print(result)

    # Test 2: Read from inaccessible file
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd")
    print(result)

    # Test 3: Read from existing file
    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    # Test 4: Write to file
    if result[0]:
        print("\nUsing 'secure_archive' to write previous content to a new file:")
        write_result = secure_archive("vault_backup.txt", "write", result[1])
        print(write_result)


if __name__ == "__main__":
    main()
