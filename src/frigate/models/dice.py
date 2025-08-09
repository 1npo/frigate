"""Defines objects related to dice"""

from dataclasses import dataclass, field
from enum import Enum

from models.perks import Perk


class DieType(Enum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10


@dataclass
class DieFace:
    value: int
    perks: list[Perk] = field(default_factory=list)


@dataclass
class Die:
    type: DieType
    faces: list[DieFace] = field(default_factory=list)
    shop_cost: int = None

    def __post_init__(self):
        self.faces = [DieFace(value=i) for i in range(1, self.type.value + 1)]


@dataclass
class DiceCollection:
    dice: list[Die] = field(default_factory=list)

    def add_die(self, die: Die):
        raise NotImplementedError()

    def remove_die(self, die: Die):
        raise NotImplementedError()

    def sell_die(self, die: Die):
        raise NotImplementedError()
