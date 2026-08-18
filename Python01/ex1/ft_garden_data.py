#!/usr/bin/env python3


class Plant:
    name: str
    height: str
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = "25cm"
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = "80cm"
    sunflower.age = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = "15cm"
    cactus.age = 120

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
