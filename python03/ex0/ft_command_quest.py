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
        i = 1
        for arg in args[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
