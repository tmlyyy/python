#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "string" + 5  # type: ignore


def test_error_types() -> None:
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
            print("Operation completed successfully")
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as e:
            print(f"Caught {type(e).__name__}: {e}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
