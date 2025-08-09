import typing as t
from dataclasses import dataclass, field

from models.dice import Die


class ScoringCalculationProtocol(t.Protocol):
    def __call__(self, hand: list[Die]) -> int: ...


def _scoring_calculation(hand: list[Die]) -> int:
    raise NotImplementedError('Calculation function must be provided when initialized')


@dataclass
class ScoringCategory:
    name: str
    level: int = 1
    calculation: ScoringCalculationProtocol = field(
        default_factory=lambda: _scoring_calculation
    )
    bonus: int = 0
    multiplier: float = 0.0
    reward: int = 0
    score: float = None


@dataclass
class Scorecard:
    categories: list[ScoringCategory] = field(default_factory=list)
