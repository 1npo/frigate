from dataclasses import dataclass
from enum import Enum, auto


class ModificationTrigger(Enum):
    BEFORE_SCORING = auto()
    BEFORE_HAND = auto()
    BEFORE_ROUND = auto()
    AFTER_SCORING = auto()
    AFTER_HAND = auto()
    AFTER_ROUND = auto()
    WHEN_SCORING = auto()
    WHEN_HAND_START = auto()
    WHEN_HAND_END = auto()
    WHEN_ROUND_START = auto()
    WHEN_ROUND_END = auto()
    WHEN_PERK_CREATED = auto()
    WHEN_PERK_DESTROYED = auto()
    WHEN_PERK_IN_INVENTORY = auto()
    WHEN_PERK_SOLD = auto()
    WHEN_PERK_PURCHASED = auto()
    WHEN_HAND_PLAYED = auto()
    WHEN_SHOP_OPENS = auto()
    WHEN_SHOP_CLOSES = auto()


class ModificationAction(Enum):
    CREATE = auto()  # Create something with a perk or by purchasing it
    DELETE = auto()  # Delete something with a perk or by selling it
    REPLACE = auto()  # Delete and then create something
    MODIFY = auto()  # Add a modification to something
    SET_VALUE = auto()  # Set the value of something to a specific number
    INCREASE = auto()  # Increase the value of something
    DECREASE = auto()  # Decrease the value of something


class ModifiedObject(Enum):
    PERK = auto()
    PERK_MODIFIER = auto()
    PERK_COST = auto()
    DIE = auto()
    DIE_COST = auto()
    DIE_FACE_VALUE = auto()
    DIE_FACE_MODIFIER = auto()
    REROLL_COST = auto()
    CATEGORY = auto()
    CATEGORY_COST = auto()
    CATEGORY_LEVEL = auto()
    CATEGORY_BONUS = auto()
    CATEGORY_MULTIPLIER = auto()
    CATEGORY_REWARD = auto()
    INVENTORY_SIZE = auto()
    HAND_SIZE = auto()
    HAND_SCORE_BONUS = auto()
    HAND_SCORE_MULT = auto()
    ROUND_SCORE_BONUS = auto()
    ROUND_SCORE_MULT = auto()
    MODIFICATION_VALUE = auto()


@dataclass
class Modification:
    name: str
    description: str
    trigger: ModificationTrigger
    modifies: ModifiedObject
    action: ModificationAction


class PerkEdition(Enum):
    STANDARD = auto()
    HOLOGRAPHIC = auto()
    POLYCHROME = auto()


class PerkRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    LEGENDARY = auto()


class PerkDuration(Enum):
    PERMANENT = auto()
    TEMPORARY = auto()
    INSTANT = auto()


class PerkMode(Enum):
    ACTIVE = auto()
    PASSIVE = auto()


@dataclass
class Perk:
    name: str
    modifications: list[Modification]
    cost: int
    edition: PerkEdition
    rarity: PerkRarity
    duration: PerkDuration
    mode: PerkMode


@dataclass
class Parameters:
    verbose: bool


def parse_user_args(args: list) -> Parameters:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
