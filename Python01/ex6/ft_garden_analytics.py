#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8
    ) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.growth_rate: float = growth_rate
        self._stats: Plant.Stats = self.Stats()
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> Stats:
        return self._stats

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def show(self) -> None:
        self._stats.increment_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.increment_grow()
        self.set_height(self.get_height() + self.growth_rate)

    def age(self, days: int = 1) -> None:
        self._stats.increment_age()
        self.set_age(self.get_age() + days)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth_rate: float = 8.0
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.get_name()} is blooming beautifully!")
        else:
            print(f"{self.get_name()} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._stats: Tree.TreeStats = self.TreeStats()

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        h = self.get_height()
        d = self.trunk_diameter
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{h:.1f}cm long and {d:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth_rate: float = 30.0
    ) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seeds: int = 0

    def bloom(self, seeds: int = 42) -> None:
        super().bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print()

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_plant_stats(sunflower)
    print()

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_plant_stats(anon)


if __name__ == "__main__":
    main()
