"""Run a round-robin tournament of factory and strategy pairs."""

from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (AggressiveStrategy, BattleStrategy, InvalidStrategyError,
                 NormalStrategy)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    """Run every unordered pair once; propagate an incompatible strategy."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for left_index in range(len(opponents)):
        for right_index in range(left_index + 1, len(opponents)):
            left_factory, left_strategy = opponents[left_index]
            right_factory, right_strategy = opponents[right_index]
            left = left_factory.create_base()
            right = right_factory.create_base()
            print("\n* Battle *")
            print(left.describe())
            print(" vs.")
            print(right.describe())
            print(" now fight!")
            left_strategy.act(left)
            right_strategy.act(right)


if __name__ == "__main__":
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    print("Tournament 0 (basic)")
    battle([(flame, normal), (transform, aggressive)])
    print("\nTournament 1 (error)")
    try:
        battle([(transform, aggressive), (flame, aggressive)])
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")
