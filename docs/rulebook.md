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
      - [Perk Durations](#perk-durations)
      - [Perk Modes](#perk-modes)
      - [Perk Rarities](#perk-rarities)
      - [Perk Editions](#perk-editions)
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

Win a round of Frigate by playing Yahtzee-style dice hands until your score matches or exceeds the round's score target. Each round has a higher score target than the previous round. Win a game (run) by winning 15 rounds. 

## Components

You start each run with a scorecard, a collection of 5 D6 dice, 3 random perks in an inventory that holds 5 perks, and a wallet containing a small amount of starting money. Perks modify almost every aspect of the game. After every 5 hands, a shop appears where you can spend money to buy new perks and scorecard categories.

### Scorecard

You start with a base scorecard that has 15 categories of hands you can play. Each category has a scoring calculation, a bonus, a multiplier, a reward, and a scoring box. Categories can be upgraded to permanently increase their bonus, multiplier, and reward.

Additional hand categories become available to purchase in the shop when you have the dice needed to play those hands. For example, the "Eights" category becomes available when your dice set includes at least one D8. See [categories.md](categories.md) for an exhaustive list of all categories and their details.

### Dice

You start with a set of 5 D6 dice. Perks enable you to add, remove, or modify dice in your collection. They can also change the numbers on the faces of your die, and they can add permanent modifiers to die faces. You can add an unlimited number of dice to your collection. The available types of dice are D4, D6, D8, and D10.

### Perks

Perks modify how the game works. There are 4 types of perks: dice perks, scoring perks, inventory perks, and shop perks. Each perk modifies something about that game component, and has a duration, mode, rarity, and edition. See [perks.md](perks.md) for an exhaustive list of all perks and their details.

#### Perk Durations

The duration of a perk indicates how long it exists in your inventory. There are 3 durations:

- **Permanent** perks remain in effect until the perk is destroyed or sold.
- **Temporary** perks expire after a certain duration (usually after some number of hands or rounds).
- **One-time** perks are destroyed immediately after they're activated 

#### Perk Modes

The mode indicates how the perk is activated. There are 3 modes:

- **Active** perks apply their modifications when they're used by the player in the rolling phase of a hand.
- **Queued** perks apply their modifications when they're evaluated in the scoring phase of a hand.
- **Passive** perks apply their modifications automatically when some condition is met.

#### Perk Rarities

The rarity indicates how impactful the perk is, and how likely you are to start with it or find it in the shop. The rarer a perk is, the more impactful it is to the game, and the harder it is to find. There are 4 rarities:

- **Common** perks have a %70 chance of appearing.
- **Uncommon** perks have a %20 chance of appearing.
- **Rare** perks have a %12 chance of appearing.
- **Legendary** perks have a %3 chance of appearing.

#### Perk Editions

The edition indicates how many additional modifications a perk applies. There are 3 editions:

- **Standard** edition perks have 0 additional modifications
- **Foil** edition perks have 1 additional modification
- **Holographic** edition perks have 2 additional modifications

### Money

You start each run with a small amount of money in your wallet. Money is added to your wallet after you play each hand that scores more than 0 points. Perks can add money to your wallet and take money out of it. You can sell perks in your inventory at any time. Money is spent in the shop.

### Shop

At the end of every 5 hands, the game pauses and the shop opens. The shop shows 2 random perks of each type, 5 random dice for purchase, and all scorecard categories available for purchase or upgrade. The shop can be re-stocked with a new set of random items for a cost. You can buy any or all the items in the shop, if you have enough money and enough space in your inventory and collection. You can also choose to close the shop without spending any money. Once you close the shop, it won't be available again until it opens in another 5 hands.

## Gameplay

A run of Frigate consists of 15 rounds, with a variable number of hands in each round. You keep playing hands until you've either played every category of hand on your scorecard, or your round score matches or exceeds the round's score target -- whichever comes first. You win the round if your score meets or exceeds the score target. You lose the run if your score is less than the score target after playing every hand on your scorecard. Win the run by winning 15 rounds.

### Game Board

There are 7 areas of the game board:

- **Run, Round, Hand, and Wallet Details** - Shows the current numbers and scores
- **Scorecard** - All available categories with their details and score boxes
- **Perk inventory** - All owned perks that are available to use
  - Size of perk inventory is limited, but can be increased by using certain perks
- **Perk queue** - One-time perks are placed here to be used (and then destroyed) when the hand is played 
- **Dice collection** - Pool of all dice that are available to use for rolling hands
  - Size of collection is unlimited, is increased whenever new dice are added
- **Throwing tray** - Dice being rolled for a hand are stored and rolled here
- **Dice queue** - Rolled dice are arranged in this queue to be played as a hand

### Playing Hands

Each hand consists of two phases: rolling and scoring.

The starting hand size is 5 dice. It can be reduced to a minimum of 2 dice, and increased to a maximum of 8 dice. A full hand must be played every hand. So if the hand size is 5, then 5 dice must be played every hand. And if the hand size is 8, then 8 dice must be played every hand.

#### Rolling Phase

Each hand begins with the rolling phase:

1. Select N dice from your collection for this hand, where N is the current hand size, and place them in the tray (if you don't already have any dice in the tray)
2. Roll all the dice in the tray to determine your hand
3. Move any dice you want to keep into the dice queue
4. Re-roll any dice you leave in the tray
5. Repeat steps 2-3 until no re-rolls remain, or all the dice are queued to play
6. Add any perks to the perk queue
7. Select an available scoring box to play your hand in
8. Play your hand
9. Go to the scoring phase

Perks can be sold, and active perks can be used, at any time during the rolling phase.

You must enter a hand into a scoring box on your scorecard every round. The scorng box in each category can only be filled in once per round (unless modified by a perk).

#### Scoring Phase

Each hand ends with the scoring phase. The scoring happens automatically in the order listed below:

1. Apply any perks that modify the category bonus
2. Apply any perks that modify the category multiplier
3. For each die in the queue from left to right:
   1. Add the face value to the category score box
   2. Apply any modifiers on the die face
4. Add the category bonus to the score box
5. Multiply the value in the score box by the category multiplier
   - This is your hand score
6. Apply any perks that modify your hand score
7. Add your hand score to your round score
8. Apply any perks that modify your round score, if this is the last hand in the round
9.  Apply any perks that modify the category reward
10. Add the category reward to your wallet

### Playing Rounds

A round ends when there are no more playable categories on your scorecard, or your total round score is equal to or greater than the round's score target.

If there are no more available categories, and your total round score is less than the score target, then the run ends and you lose. Otherwise you win the round, then all the scoring boxes on your scorecard are emptied, and the next round begins.

When you win round 15, you win the run, and can choose to continue playing in "endless" mode.

## Boss Rounds

Rounds 3, 6, 9, and 12 are boss rounds, and round 15 is the final boss. Boss rounds apply a random debuff to all hands in the round. The pool of available debuffs is different for each boss round. So any debuff that appears in round 5 will never appear in round 10 or 15. Debuffs become more impactful and potentially run ending as the rounds progress towards the final boss.

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

- D4 - 35%
- D6 - 45%
- D8 - 15%
- D10 - 5%
