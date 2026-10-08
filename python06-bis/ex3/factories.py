"""Factories return creatures through their abstract interface."""

from abc import ABC, abstractmethod

from .creatures import Creature, Flameling, Morphagon, Pyrodon, Shiftling


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Create a base creature."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create an evolved creature."""


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
