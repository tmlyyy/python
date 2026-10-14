"""Interchangeable battle actions selected by creature capability."""

from abc import ABC, abstractmethod

from ex3.creatures import Creature, TransformCapability


class InvalidStrategyError(ValueError):
    """A strategy was asked to act on an incompatible creature."""


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Report whether this strategy can act on the creature."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Perform this strategy's battle action."""


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for aggressive strategy"
            )
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            try:
                print(creature.attack())
            finally:
                print(creature.revert())
