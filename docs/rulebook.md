# Rulebook

This rulebook explains how to play Frigate.

## Content

- [Rulebook](#rulebook)
  - [Content](#content)
  - [Objective](#objective)
  - [Components](#components)
    - [Scorecard](#scorecard)
    - [Dice](#dice)
    - [Perks](#perks)
      - [Description](#description)
      - [Types](#types)
      - [Durations](#durations)
      - [Perk Modes](#perk-modes)
      - [Rarities](#rarities)
      - [Targets](#targets)
      - [Actions](#actions)
      - [Values](#values)
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
  - [Chances](#chances)

## Objective

Win a round of Frigate by playing Yahtzee-style dice hands until your score matches or exceeds the round's score target. Each round has a higher score target than the previous round. So you build a scoring engine with dice and perks that can keep up with the increased score targets. Win a game (run) by winning 15 rounds. 

## Components

You start each run with the following:

- A scorecard that lists a set of 15 scoring categories
- A collection of 5 D6 dice
- 3 random perk cards in an inventory that holds 5 cards
- A wallet containing $5 of starting money
- A tray where you place the dice you'll roll
- A queue where you arrange the rolled dice into hands

### Scorecard

You start with a scorecard that has 15 categories of hands you can play. Each scoring category has the following attributes:

- A level
- A scoring calculation
- A bonus
- a multiplier
- A reward
- A a scoring box

Category levels can be upgraded to permanently increase their bonus, multiplier, and reward. Additional scoring categories become available to purchase in the shop when you have the dice needed to play those hands. For example, the "Eights" category becomes available when your dice set includes at least one D8.

See [docs/categories.md](categories.md) for an exhaustive list of all categories and their details.

### Dice

You start with a set of 5 D6 dice. Perk cards can be used to add, remove, or modify dice in your collection. They can also change the values on die faces and apply perks to them. Dice purchased in the shop will occasionally have perks on one or more of their faces. You can add an unlimited number of dice to your collection. The available types of dice are D4, D6, D8, and D10.

### Perks

A perk modifies something about one or more game components, and has the following attributes:

- Name
- Description
- Type
- Duration
- Mode
- Rarity
- Target
- Action
- Value
- Trigger (optional)
- Condition (optional)

See [docs/perks.md](perks.md) for an exhaustive list of all perks and their details.

#### Description

The description of a perk describes the duration, mode, target, action, value, trigger, and duration of the perk. The description uses a consistent naming and phrasing scheme. For example, the perk descriptions contain the following attributes:

- `Create 1 random Uncommon perk when Small Straight is scored with a hand of 1,2,3,4`
  - **Duration** -> Permanent
  - **Target** -> random Uncommon perk 
  - **Action** -> Create
  - **Value** -> 1
  - **Trigger** -> Score a Small Straight
  - **Condition** -> Hand contains 1,2,3,4

- `Gain +1 multiplier every time {category} is scored (category changes at end of hand, currently +?)`
  - **Duration** -> Permanent
  - **Target** -> The perk card itself
  - **Action** -> Add
  - **Value** -> 1
  - **Trigger** -> Category is scored

#### Types

There are two types of perks: perk cards and dice perks. Perk cards are cards that appear in your inventory and can be purchased in the shop. Dice perks are perks applied to die faces.

#### Durations

The duration indicates how long the perk exists in your inventory. There are 3 durations:

- **Permanent** perks remain in effect until the perk is destroyed or sold
- **Temporary** perks expire after a certain duration (usually after some number of hands or rounds)
- **One-time** perks are destroyed immediately after they're activated

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

#### Targets

Perks target one or more of these game components:

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

#### Actions

Perks perform one or more of these actions on the target:

- Set a value
- Add a value
- Subtract a value
- Multiply a value
- Create an object
- Destroy an object
- Disable an object

Dice and perk cards can be created, destroyed, or disabled. Scorecard categories can only be created. Debuffs can only be disabled. Every other game component that's modified by a perk is a number that's set, added to, subtracted from, or multiplied.

#### Values

The value of a perk is the amount that the target is modified by, or the name of the object being created, destroyed, or disabled. For example, in this perk description, the value is 1: `Add $1 to category reward for each die in collection`.

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

Perks can be sold, and active perks can be used, at any time during the rolling phase.

You must enter a hand into a scoring box on your scorecard every round. The scoring box in each category can only be filled in once per round. Some perks can increase the number of times you can score a category in a round.

#### Scoring Phase

Each hand ends with the scoring phase. The scoring happens automatically in the order listed below:

1. Apply any perks that modify the category bonus
1. Apply any perks that modify the category multiplier
1. For each die in the queue from left to right:
   1. Add the face value to the category score box
   1. Apply any perks on the die face
1. Add the category bonus to the score box
1. Multiply the value in the score box by the category multiplier
   - This is your hand score
1. Apply any perks that modify your hand score
1. Add your hand score to your round score
1. Apply any perks that modify your round score, if this is the last hand in the round
1. Apply any perks that modify the category reward
1. Add the category reward to your wallet
2. Go to the next hand

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

## Chances

These are the chances for each dice type to appear for purchase in the shop:

- D4 - 20%
- D6 - 60%
- D8 - 15%
- D10 - 5%
