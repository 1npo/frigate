from dataclasses import dataclass, field
from enum import Enum

MAX_DICE_IN_SET = 8
MAX_REROLLS_AT_START = 2


class DieType(Enum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10


@dataclass
class Die:
    type: DieType
    faces: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.faces = [i for i in range(1, self.type.value + 1)]


@dataclass
class DiceSet:
    dice: list[Die]
    hold: list[Die] = field(default_factory=list)
    rerolls: int = MAX_REROLLS_AT_START
