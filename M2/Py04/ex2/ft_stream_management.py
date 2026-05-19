import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        sys.stderr.write("[STDERR] Usage: ft_stream_management.py <file>\n")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO = open(filename)
        print("---")
        content: str = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return

    # Transform data
    lines: list[str] = content.split('\n')
    transformed_lines: list[str] = [line + '#' for line in lines]
    transformed_content: str = '\n'.join(transformed_lines)

    print("Transform data:")
    print("---")
    print(transformed_content)
    print("---")

    # Ask for filename without using input()
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename: str = sys.stdin.readline().strip()

    if not new_filename:
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{new_filename}'")
        output_file: IO = open(new_filename, 'w')
        output_file.write(transformed_content)
        output_file.close()
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_filename}': {e}\n"
        )
        print("Data not saved.")


if __name__ == "__main__":
    main()