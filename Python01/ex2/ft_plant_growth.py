#!/usr/bin/env python3


class Plant:
    name: str
    height: float
    days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30

    start_height = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    weekly_growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {weekly_growth:.1f}cm")


if __name__ == "__main__":
    main()
