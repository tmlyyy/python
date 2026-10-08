#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    _, filename = sys.argv

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        content: str = file_obj.read()
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
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    main()
