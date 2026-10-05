#!/usr/bin/env python3
def secure_archive(
    filename: str,
    action: str = "read",
    content: str | None = None,
) -> tuple[bool, str]:
    try:
        if action == "write":
            write_content = content if content is not None else ""
            with open(filename, "w") as f:
                f.write(write_content)
            return (True, "Content successfully written to file")
        if action == "read":
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)
        return (False, f"Unsupported action: {action}")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    res_none = secure_archive("/not/existing/file")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(res_none)

    res_perm = secure_archive("/etc/master.passwd")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(res_perm)

    res_ok = secure_archive("ancient_fragment.txt")
    print("Using 'secure_archive' to read from a regular file:")
    print(res_ok)

    success, previous_content = res_ok

    if success:
        res_write = secure_archive(
            "vault_output.txt", "write", previous_content
        )
        print(
            "Using 'secure_archive' to write previous content to a new file:"
        )
        print(res_write)
    else:
        print("Skipping the write because the archive could not be read.")


if __name__ == "__main__":
    main()
