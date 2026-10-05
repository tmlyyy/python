#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    for temp_str in ("25", "abc"):
        print(f"Input data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
