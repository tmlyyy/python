#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    args = sys.argv

    program_name = args[0].split("/")[-1]
    print(f"Program name: {program_name}")

    num_args = len(args) - 1

    if num_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_args}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
