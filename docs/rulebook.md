# Rulebook

This rulebook explains how to play Frigate.

## Content

- [Rulebook](#rulebook)
  - [Content](#content)
  - [Objective](#objective)
  - [Components](#components)
    - [Scorecard](#scorecard)
      - [Scorecard Categories](#scorecard-categories)
        - [Base Categories](#base-categories)
        - [Purchaseable Categories](#purchaseable-categories)
    - [Dice](#dice)
    - [Perks](#perks)
      - [Categories](#categories)
      - [Modifications](#modifications)
      - [Modified Components](#modified-components)
      - [Durations](#durations)
      - [Perk Modes](#perk-modes)
      - [Rarities](#rarities)
      - [Inventory](#inventory)
    - [Money](#money)
    - [Shop](#shop)
  - [Gameplay](#gameplay)
    - [Game Board](#game-board)
    - [Playing Hands](#playing-hands)
      - [Rolling Phase](#rolling-phase)
      - [Scoring Phase](#scoring-phase)
    - [Playing Rounds](#playing-rounds)
  - [Boss Rounds](#boss-rounds)
  - [Unlocking Features](#unlocking-features)
    - [Perks](#perks-1)
    - [Difficulty Levels](#difficulty-levels)
      - [Level Scaling](#level-scaling)
      - [Debuffs](#debuffs)

## Objective

Win a round of Frigate by playing Yahtzee-style dice hands until your score matches or exceeds the round's score target. Each round has a higher score target than the previous round. Build a scoring engine with dice and perks to keep up with the increased score targets. Win a game (run) by winning 15 rounds. 

## Components

You start each run with the following:

- A scorecard that lists 15 scoring categories
- A collection of 5 D6 dice
- 3 random perk cards in an inventory that holds 5 cards
- A wallet containing $5 of starting money
- A tray where you place the dice you'll roll
- A queue where you arrange the rolled dice into hands

### Scorecard

You start with a scorecard that has 15 categories of hands you can play. Each scoring category has the following attributes:

- A level
- A score calculation
- A bonus
- A multiplier
- A reward
- A scoring box

The score calculation determines how rolled dice are summed to get your base points. Bonus points are additional points added to your base points. The resulting score is then multiplied by the multiplier. Category levels can be upgraded to permanently increase their bonus, multiplier, and reward. Additional scoring categories become available to purchase in the shop when you have the dice needed to play those hands. For example, the "Eights" category becomes available when your dice set includes at least one D8.

#### Scorecard Categories

##### Base Categories

| Category | Score Calculation | Base Score Bonus | Base Score Multiplier | Base Reward | Upgrading Adds Score / Bonus |
| --- | --- | --- | --- | --- | --- |
| Aces | Sum of all dice with 1 | +2 | x2 | $1 | +2 / x1 |
| Twos | Sum of all dice with 2 | +2 | x2 | $1 | +2 / x1 |
| Threes | Sum of all dice with 3 | +2 | x2 | $1 | +2 / x1 |
| Fours | Sum of all dice with 4 | +2 | x2 | $1 | +2 / x1 |
| Fives | Sum of all dice with 5 | +2 | x2 | $1 | +2 / x1 |
| Sixes | Sum of all dice with 6 | +2 | x2 | $1 | +2 / x1 |
| Wild | Sum of all dice | +2 | x2 | $1 | +2 / x1 |
| Pair | Sum of the 2 paired dice | +4 | x2 | $1 | +4 / x1 |
| *Two Pair | Sum of the 4 dice | +4 | x2 | $1 | +4 / x1 |
| *Full House | Sum of all 5 dice | +6 | x2 | $1 | +6 / x1 |
| *Three of a Kind | Sum of the 3 dice | +6 | x2 | $1 | +6 / x1 |
| *Four of a Kind | Sum of the 4 dice | +6 | x2 | $1 | +6 / x1 |
| *Five of a Kind | Sum of the 5 dice | +8 | x3 | $2 | +8 / x1 |
| *Small Straight | Sum of the 4 consecutive dice | +8 | x3 | $2 | +8 / x1 |
| *Large Straight | Sum of all 5 consecutive dice | +8 | x3 | $2 | +8 / x1 |

\* This category will become deactivated if the current hand size is reduced to less than 5 dice. It will be reactivated once the hand size returns to >= 5.

##### Purchaseable Categories

Each of these categories will be deactivated if the availability requirements are no longer met. If the availability requirements are met again, the category will be reactivated without needing to be re-purchased.

| Category | Score Calculation | Base Score Bonus | Base Score Multiplier | Base Reward | Upgrading Adds Score / Bonus | Cost in Shop | Availability Requirements |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sevens | Sum of all dice with 7 | +2 | x2 | $1 | +2 / x1 | $2 | At least 1 D8 or D10 in collection |
| Eights | Sum of all dice with 8 | +2 | x2 | $1 | +2 / x1 | $2 | At least 1 D8 or D10 in collection |
| Nines | Sum of all dice with 9 | +2 | x2 | $1 | +2 / x1 | $2 | At least 1 D10 in collection |
| Tens | Sum of all dice with 10 | +2 | x2 | $1 | +2 / x1 | $2 | At least 1 D10 in collection |
| Triple Pair | Sum of the 6 dice | +8 | x3 | $2 | +8 / x1 | $3 | Hand size is at least 6 |
| Double Two Pair | Sum of the 8 dice | +8 | x3 | $2 | +8 / x1 | $3 | Hand size is 8 |
| Double Small Straight | Sum of the 8 dice | +14 | x3 | $3 | +14 / x2 | $4 | Hand size is 8 |
| Full Straight | Sum of the 6-8 dice | +14 | x3 | $3 | +14 / x2 | $4 | Hand size is at least 6 |
| Six of a Kind | Sum of the 6 dice | +16 | x4 | $4 | +16 / x3 | $4 |  Hand size is at least 6 |
| Seven of a Kind | Sum of the 7 dice | +18 | x5 | $4 | +18 / x3 | $4 | Hand size is at least 7 |
| Eight of a Kind | Sum of the 8 dice | +20 | x6 | $4 | +20 / x3 | $4 | Hand size is 8 |

### Dice

You start with a set of 5 D6 dice. Perk cards can be used to add, remove, or modify dice in your collection. They can also change the values on die faces and apply modifications to them. Dice purchased in the shop will occasionally have modifications on one or more of their faces. You can add an unlimited number of dice to your collection. The available types of dice are D4, D6, D8, and D10.

### Perks

A perk modifies something about one or more game components. There are two types of perks: perk cards and dice perks. Perk cards are cards that appear in your inventory and can be purchased in the shop. Dice perks are modifications applied to die faces.

See [docs/all_perks.csv](all_perks.csv) for a comprehensive list of all perks and their attributes.

#### Categories

All perks (both perk cards and dice perks) belong to one or more of these 3 categories:

- **Economy** perks influence your wallet, how much money you make, how much things cost in the shop, and how much perks and dice sell for
- **Scoring** perks influence your hand score, your round score, and the level and scoring of scorecard categories
- **Support** perks influence your perk card inventory and dice collection, and round debuffs

#### Modifications

Perks perform one or more of these actions when modifying a game component:

- Set a value
- Add a value
- Subtract a value
- Multiply a value
- Create an object
- Destroy an object
- Disable an object

Dice and perk cards can be created, destroyed, or disabled. Scorecard categories can only be created or disabled. Debuffs can only be disabled. Every other game component that's modified by a perk is a number that's set, added to, subtracted from, or multiplied.

#### Modified Components

Perks modify one or more of these game components:

- Dice
- Dice faces
- Category bonus
- Category mult
- Category reward
- Category level
- Hand size
- Hand score
- Round score
- Round debuff
- Rolling phase
- Scoring phase
- Shop cost
- Shop stock
- Perk card
- Perk value
- Inventory size

#### Durations

The duration indicates how long the perk exists in your inventory. There are 3 durations:

- **Permanent** perks remain in effect until the perk is destroyed or sold
- **Temporary** perks expire after a certain duration (usually after some number of hands or rounds)
- **Consumable** perks can be used one or more limited number of times, and are then destroyed

#### Perk Modes

The mode indicates how the perk is activated. There are 2 modes:

- **Active** perks apply their modifications when they're used by the player
- **Passive** perks apply their modifications automatically when some condition is met

#### Rarities

The rarity indicates how impactful the perk is, and how likely you are to start with it or find it in the shop. The rarer a perk is, the more impactful it is to the game, and the harder it is to find. There are 4 rarities:

- **Common** perks have a %60 chance of appearing
- **Uncommon** perks have a %25 chance of appearing
- **Rare** perks have a %10 chance of appearing
- **Legendary** perks have a %5 chance of appearing

#### Inventory

Your inventory can hold a max of 5 perk cards when the run starts. Perks can be used to increase or decrease the maximum number of slots in your inventory. There's no limit to how many slots your inventory can have.

### Money

You start each run with a small amount of money in your wallet. Money is added to your wallet after you play each hand that scores more than 0 points. Perks can add money to your wallet and take money out of it. You can sell perks in your inventory at any time. Money is spent in the shop.

### Shop

After every 5 hands, the game pauses and a shop appears with the following items for purchase:

- 5 random perk cards
- 5 random dice
- Available scorecard categories
- Available scorecard upgrades

The shop can be re-stocked with a new set of random items for a cost. You can buy any or all the items in the shop, if you have enough money and enough space in your inventory and collection. You can also choose to close the shop without spending any money. Once you close the shop, it won't be available until it opens again in another 5 hands.

## Gameplay

A run of Frigate consists of 15 rounds, with a variable number of hands in each round. You keep playing hands until you've either played every category of hand on your scorecard, or your round score matches or exceeds the round's score target -- whichever comes first. If your score meets or exceeds the score target, you win the round. If your score is less than the score target after playing every hand on your scorecard, you lose the round and the run. Win the run by winning all 15 rounds.

### Game Board

There are 8 areas of the game board:

- **Details** - Shows the current Run, Round, Hand, and Wallet numbers & scores
- **Scorecard** - All available categories and their attributes
- **Perk card inventory** - Ordered arrangement of all perk cards that are available to use
- **Dice collection** - Drawer of all dice that are available to use for rolling hands
- **Throwing tray** - Dice being rolled for a hand are stored and rolled here
- **Dice queue** - Rolled dice are arranged in this queue to be played as a hand
- **Control panel** - Contains the buttons that:
  - (Re-)roll your dice
  - Play your hand
  - Use a perk card
  - Sell a perk card
  - Show your dice collection
  - Show the game documentation
  - Open the menu

### Playing Hands

Each hand consists of two phases: rolling and scoring.

The starting hand size is 5 dice. It can be reduced to a minimum of 2 dice, and increased to a maximum of 8 dice. A full hand must be played every hand. So if the hand size is 5, then 5 dice must be played every hand. And if the hand size is 8, then 8 dice must be played every hand.

#### Rolling Phase

Each hand begins with the rolling phase:

1. Place N dice in the tray (N = current hand size)
1. Roll all the dice in the tray to determine your hand
1. Move any dice you want to keep into the dice queue
1. Re-roll any dice you leave in the tray
1. Repeat steps 2-3 until no re-rolls remain, or all the dice are queued to play
1. Select an available scoring box to play your hand in
1. Play your hand
1. Go to the scoring phase

Dice and perk cards can be sold, and active perks can be used, at any time during the rolling phase.

You must enter a hand into a scoring box on your scorecard every round. The scoring box in each category can only be filled in once per round. Some perks can increase the number of times you can score a category in a round.

#### Scoring Phase

Each hand ends with the scoring phase. The scoring happens automatically in the order listed below:

1. For each perk in your inventory from left to right:
   1. Apply any perk that modifies the category bonus
   2. Apply any perk that modifies the category multiplier
2. For each die in the queue from left to right:
   1. Add the face value to the category score box
   2. Apply any perks on the die face
3. Add the category bonus to the score box
4. Multiply the value in the score box by the category multiplier
   - This is your hand score
5. Apply any perks in your inventory that modify your hand score, from left to right
6. Add your hand score to your round score
7. If this is the last hand in the round: Apply any perks that modify your round score, from left to right
8.  Apply any perks in your inventory that modify the category reward, from left to right
9.  Add the category reward to your wallet
10. Go to the next hand

### Playing Rounds

A round ends when there are no more playable categories on your scorecard, or your total round score is equal to or greater than the round's score target.

If there are no more available categories, and your total round score is less than the score target, then the run ends and you lose. Otherwise you win the round, then all the scoring boxes on your scorecard are emptied, and the next round begins.

When you win round 15, you win the run, and can choose to continue playing in "endless" mode.

## Boss Rounds

Rounds 3, 6, 9, and 12 are boss rounds, and round 15 is the final boss. Boss rounds apply a random debuff to all hands in the round. The pool of available debuffs is different for each boss round. So any debuff that appears in round 5 will never appear in round 10 or 15. Debuffs become more impactful and potentially run-ending as the rounds progress to the final boss.

## Unlocking Features

### Perks

Not all perks are immediately available. Some perks need to be unlocked by completing challenges. See [perks.md](perks.md) for which perks need to be unlocked and how to unlock them.

### Difficulty Levels

You can choose the game difficulty when starting a new run. Only one difficulty level is available at the start. Winning a run on one difficulty unlocks the next difficulty level. Each successive level has a higher score target, and may include debuffs.

#### Level Scaling

The score target of each round is calculated using a scaling function. Increasing the difficulty level changes this scaling function. As the difficulty increases, the score targets get larger, and how much the score target increases from round to round also gets larger.

*The scaling function is TBD and will be worked out through trial and error during development.*

*Add description of scaling function here once determined.*

#### Debuffs

Higher difficulty levels also have debuffs that apply for the whole run.

*For example, all scorescard categories give -1 bonus and -1 multiplier.*

*Debuffs are TBD and will be worked out through trial and error during development.*

*Add description or table of debuffs here once determined.*
