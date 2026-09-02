#!/usr/bin/env python3
import typing


def secure_archive(
    filename: str,
    action: typing.Union[int, str] = "read",
    content: typing.Optional[str] = None,
) -> tuple[bool, str]:
    is_write = False
    if action == 1 or action == "write":
        is_write = True

    try:
        if is_write:
            write_content = content if content is not None else ""
            with open(filename, "w") as f:
                f.write(write_content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    # Teste 1: Lendo arquivo inexistente (com o "a" igual ao PDF)
    res_none = secure_archive("/not/existing/file")
    print(
        f"Using 'secure_archive' to read from a nonexistent file: {res_none}"
    )

    # Teste 2: Lendo arquivo inacessível (com o "an" igual ao PDF)
    res_perm = secure_archive("/etc/master.passwd")
    print(
        f"Using 'secure_archive' to read from an inaccessible file: "
        f"{res_perm}"
    )

    # Teste 3: Lendo do arquivo regular
    res_ok = secure_archive("ancient_fragment.txt")
    print(f"Using 'secure_archive' to read from a regular file: {res_ok}")

    # Desempacotamos o retorno do Teste 3 para pegar o conteúdo lido
    success, previous_content = res_ok

    # Teste 4: Escrevendo o "previous content" no novo arquivo (igual ao PDF)
    res_write = secure_archive(
        "vault_output.txt",
        "write",
        previous_content if success else ""
    )
    print(
        f"Using 'secure_archive' to write previous content to a new file: "
        f"{res_write}"
    )


if __name__ == "__main__":
    main()
