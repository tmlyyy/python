"""Exercise transformation on both members of the transform family."""

from ex3 import TransformCreatureFactory
from ex3.creatures import TransformCapability


def main() -> None:
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    for label, creature in (("base", factory.create_base()),
                            ("evolved", factory.create_evolved())):
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    main()
