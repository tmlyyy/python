#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    # Desempacotamento de lista para evitar Ã­ndices numÃ©ricos com colchetes
    _, filename = sys.argv
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.Optional[typing.IO[str]] = None
    content: str = ""
    try:
        file_obj = open(filename, "r")
        content = file_obj.read()
        print("---")
        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)
        file_obj.close()
        file_obj = None
        print(f"---File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if file_obj is not None:
            file_obj.close()

    print("Transform data:")
    print("---")

    # Processamos linha por linha para adicionar o marcador de 2087 (#)
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [line + "#" for line in lines if line]
    new_content: str = "\n".join(transformed_lines) + "\n"
    print(new_content, end="")

    try:
        new_filename: str = input("---Enter new file name (or empty): ")
    except EOFError:
        new_filename = ""

    if not new_filename.strip():
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out_file: typing.Optional[typing.IO[str]] = None
    try:
        out_file = open(new_filename, "w")
        out_file.write(new_content)
        out_file.close()
        out_file = None
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        print(f"Error saving file '{new_filename}': {e}")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
