# Perks

## Perk Attributes

- Name
- Modifications
  - Description (English sentence representation of all Modification elements)
  - Modification
    - Modification trigger
    - Modification
    - Modified object
- Cost in shop
- Edition
  - Standard
  - Holographic
  - Polychrome
- Rarity
  - Common
  - Uncommon
  - Rare
  - Legendary
- Duration
  - Permanent
  - Temporary
  - One-time
- Mode
  - Passive
  - Active

## Modified Objects

- Dice
- Die faces
- Category bonus
- Category mult
- Category reward
- Shop costs
- Perks
- Inventory

## Modification Triggers
 
- When {perk} is applied in the scoring phase
- When {die} (or {dice}) are evaluated in the scoring phase
- When used or sold by the player in the rolling phase
- When {perk} is added to or removed from inventory
- While {perk} is in your inventory
- When {category} is scored
- When round starts or ends
- When rolling phase starts
- When die in queue position {queue_pos} is evaluated
- When the shop opens or closes

## Modifications

### Dice Modifications

- Set the value of the {count} selected die faces in the queue to {value}
- Set {count} faces on selected die to {value}
- Add {modifier} to {count} selected die face(s)
- Add {count} {die_type} to collection
- Delete {count_1} {die_type_1} from collection and add {count_2} {die_type_2}

### Scoring Modifications

- Increase number of re-rolls by 1
- Increase hand size by 1 (stops appearing when hand size is the max 8)
- Increase number of times {category} can be scored in a round by 1
- Upgrade level of selected category {value} time(s)
- Upgrade level of all categories by 1
- Upgrade level of all base categories by 1
- Upgrade level of all purchased categories by 1
- Each {dice_type} in collection adds + or x {value} bonus points to {category}
- Each {dice_type} in collection adds + or x {value} multiplier to {category}
- Each {dice_type} in collection adds + or x {value} reward to {category}
- Each {dice_type} in collection adds + or x {value} bonus points to hand score
- Each {dice_type} in collection adds + or x {value} multiplier to hand score
- Each {dice_type} in collection adds + or x {value} reward to hand reward
- Each {dice_type} in collection adds + or x {value} bonus points to round score (at end of round)
- Each {dice_type} in collection adds + or x {value} multiplier to round score (at end of round)
- Each {dice_type} in collection adds + or x {value} reward to round reward (at end of round)
- Add + or x {value} bonus points to hand when die in queue is evaluated
- Add + or x {value} bonus points to hand when scored
- Add + or x {value} multiplier to hand when die in queue is evaluated
- Add + or x {value} multiplier to hand when scored
- Add + or x {value} reward to hand when die in queue is evaluated
- Add + or x {value} reward to hand when scored
- Add + or x {value} bonus points to hand when die in queue slot {slot_num} is evaluated
- Add + or x {value} bonus points to hand when die in the first/last/odd/even queue slot(s) are evaluated
- Add + or x {value} multiplier to hand when die in queue slot {slot_num} is evaluated
- Add + or x {value} multiplier to hand when die in the first/last/odd/even queue slot(s) are evaluated
- Add + or x {value} reward to hand when die in queue slot {slot_num} is evaluated
- Add + or x {value} reward to hand when die in the first/last/odd/even queue slot(s) are evaluated
- Add + or x {value} to wallet

### Inventory Modifications

- Increase inventory size by {value}
- Add {count} random perk(s) to your inventory
- Add {count} random perk(s) to your inventory when hand scores 0
- {chance} chance that the first {perk_type} in the next shop is {rarity}
- {chance} chance that the first {perk_type} in the next shop is {edition}
- Delete {count_1} {perk_type_1} from inventory and add {count_2} {die_type_2}

### Shop Modifications

- Reduce cost of re-roll in the next shop by {value}
- Reduce cost of {perk_type} in the next shop by {value}
- Reduce cost of new categories in the next shop by {value}
- Reduce cost of category upgrades in the next shop by {value}
- Reduce cost of all items in next shop by {value}

## List of Perks

See [all_perks.csv](all_perks.csv) for a comprehensive list of all perks and their attributes.

### Counts

There are 125 perks in total:

- 50 **Common** perks
- 50 **Uncommon** perks
- 20 **Rare** perks
- 5 **Legendary** perks

### List of Dice Perks

### List of Scoring Perks

### List of Inventory Perks

### List of Shop Perks
