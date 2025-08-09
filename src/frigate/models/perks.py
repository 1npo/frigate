from dataclasses import dataclass, field
from enum import StrEnum

DEFAULT_MAX_SIZE_INVENTORY = 5


class PerkType(StrEnum):
    PERK_CARD = 'Perk Card'
    DICE_PERK = 'Dice Perk'


class PerkRarity(StrEnum):
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    LEGENDARY = 'Legendary'


class PerkMode(StrEnum):
    ACTIVE = 'Active'
    PASSIVE = 'Passive'


class PerkDuration(StrEnum):
    PERMANENT = 'Permanent'
    TEMPORARY = 'Temporary'
    CONSUMABLE = 'Consumable'


class PerkCategory(StrEnum):
    ECONOMY = 'Economy'
    SCORING = 'Scoring'
    SUPPORT = 'Support'


@dataclass
class Perk:
    name: str
    description: str
    type: PerkType
    rarity: PerkRarity
    mode: PerkMode
    duration: PerkDuration
    category: PerkCategory
    mod_func: None  # TODO: Figure out how to implement this


@dataclass
class PerkCardInventory:
    perks: list[Perk] = field(default_factory=list)
    max_parks: int = DEFAULT_MAX_SIZE_INVENTORY

    def add_perk(self, perk: Perk):
        raise NotImplementedError()

    def remove_perk(self, perk: Perk):
        raise NotImplementedError()

    def disable_perk(self, perk: Perk):
        raise NotImplementedError()
