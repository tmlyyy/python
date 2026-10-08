#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    _, filename = sys.argv
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.IO[str] | None = None
    content: str = ""
    try:
        file_obj = open(filename, "r")
        content = file_obj.read()
        print("---")
        print()
        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)
        print()
        print("---")
        file_obj.close()
        file_obj = None
        print(f"File '{filename}' closed.")
    except Exception as e:
        # Requisito 1: Escreve o log de erro explicitamente no canal sys.stderr
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return
    finally:
        if file_obj is not None:
            file_obj.close()

    print("Transform data:")
    print("---")
    print()

    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [line + "#" for line in lines]
    new_content: str = "\n".join(transformed_lines)
    if content.endswith("\n"):
        new_content += "\n"
    print(new_content, end="")
    print()
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    try:
        user_input = sys.stdin.readline()
        if not user_input:
            new_filename = ""
        else:
            new_filename = user_input.rstrip("\r\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error reading input: {e}\n")
        new_filename = ""

    if not new_filename.strip():
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out_file: typing.IO[str] | None = None
    try:
        out_file = open(new_filename, "w")
        out_file.write(new_content)
        out_file.close()
        out_file = None
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error saving file '{new_filename}': {e}\n")
        print("Data not saved.")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
