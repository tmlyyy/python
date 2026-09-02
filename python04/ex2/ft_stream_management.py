#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    # Desempacotamento de lista para evitar índices numéricos com colchetes
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
        # Requisito 1: Escreve o log de erro explicitamente no canal sys.stderr
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return
    finally:
        if file_obj is not None:
            file_obj.close()

    print("Transform data:")
    print("---")

    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [line + "#" for line in lines if line]
    new_content: str = "\n".join(transformed_lines) + "\n"
    print(new_content, end="")

    # Requisito 2: Solicita o nome do arquivo usando sys.stdout e sys.stdin
    sys.stdout.write("---Enter new file name (or empty): ")
    sys.stdout.flush()

    try:
        user_input = sys.stdin.readline()
        if not user_input:
            new_filename = ""
        else:
            # Removemos a quebra de linha \n preservada pelo readline()
            new_filename = user_input.replace("\n", "").replace("\r", "")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error reading input: {e}\n")
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
        sys.stderr.write(f"[STDERR] Error saving file '{new_filename}': {e}\n")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
