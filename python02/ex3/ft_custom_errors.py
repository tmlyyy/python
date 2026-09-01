#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_function() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_function() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError... ", end="")
    try:
        test_plant_function()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError... ", end="")
    try:
        test_water_function()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        test_plant_function()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        test_water_function()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
