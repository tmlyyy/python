#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        line = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            x_str, y_str, z_str = line.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            x_str = x_str.strip()
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str}': {e}")
            continue

        try:
            y_str = y_str.strip()
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str}': {e}")
            continue

        try:
            z_str = z_str.strip()
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str}': {e}")
            continue

        if (x != x or y != y or z != z or
                x == float("inf") or y == float("inf") or
                z == float("inf") or x == float("-inf") or
                y == float("-inf") or z == float("-inf")):
            print("Coordinates must be finite numbers")
            continue

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    try:
        pos1 = get_player_pos()
    except EOFError:
        print("No more coordinates provided")
        return
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    try:
        dist1 = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    except OverflowError:
        print("Distance is too large to calculate")
        return
    if dist1 == float("inf"):
        print("Distance is too large to calculate")
        return
    print(f"Distance to center: {dist1:.4f}")

    print("Get a second set of coordinates")
    try:
        pos2 = get_player_pos()
    except EOFError:
        print("No more coordinates provided")
        return
    try:
        dist2 = math.sqrt(
            (pos2[0] - pos1[0])**2 +
            (pos2[1] - pos1[1])**2 +
            (pos2[2] - pos1[2])**2
        )
    except OverflowError:
        print("Distance is too large to calculate")
        return
    if dist2 == float("inf"):
        print("Distance is too large to calculate")
        return
    print(f"Distance between the 2 sets of coordinates: {dist2:.4f}")


if __name__ == "__main__":
    main()
