#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:

    temp_valid = "25"
    print(f"Input data is '{temp_valid}'")
    try:
        t = input_temperature(temp_valid)
        print(f"Temperature is now {t}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    temp_invalid = "abc"
    print(f"Input data is '{temp_invalid}'")
    try:
        t = input_temperature(temp_invalid)
        print(f"Temperature is now {t}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
