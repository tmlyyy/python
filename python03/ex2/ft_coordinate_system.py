#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        line = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = line.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x_str = parts[0].strip()
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str}': {e}")
            continue

        try:
            y_str = parts[1].strip()
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str}': {e}")
            continue

        try:
            z_str = parts[2].strip()
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str}': {e}")
            continue

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist1 = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {dist1:.4f}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist2 = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {dist2:.4f}")


if __name__ == "__main__":
    main()
