#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    test_cases = ["25", "abc", "100", "-50"]

    for temp_str in test_cases:
        print(f"Input data is '{temp_str}'")
        try:
            t = input_temperature(temp_str)
            print(f"Temperature is now {t}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
