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

## Objective

Win a round of Frigate by playing Yahtzee-style dice hands until your score matches or exceeds the round's score target. Each round has a higher score target than the previous round. Win a game (run) by winning 15 rounds. 

## Components

You start each run with a scorecard, a collection of 5 D6 dice, 2 random perks in an inventory that can hold 5 perks, and a wallet containing a small amount of starting money. Perks modify almost every aspect of the game. After every 5 hands, a shop appears where you can spend money to buy new perks and scorecard categories.

### Scorecard

You start with a base scorecard that has 15 hand categories. Each category has a scoring calculation, a bonus, a multiplier, a reward, and a scoring box. Categories can be upgraded to permanently increase their bonus, multiplier, and reward.

Additional hand categories become available to purchase in the shop when you have the dice needed to play those hands. For example, the "Eights" category becomes available when your dice set includes at least one D8. See [categories.md](categories.md) for an exhaustive list of all categories and their details.

### Dice

You start with a set of 5 D6 dice. Perks enable you to change the type of dice in your hand and add new dice to your collection. The available types of dice are D4, D6, D8, and D10. Perks can change the numbers on the faces of your die, and they can add permanent modifiers to die faces. You can add an unlimited number of dice to your collection.

### Perks

Perks modify how the game works. There are 3 types of perks: dice perks, scorecard perks, and inventory perks. Each perk modifies something about that game component, and has a duration, mode, rarity, and edition. See [perks.md](perks.md) for an exhaustive list of all perks and their details.

#### Perk Durations

The duration indicates how long the perk exists in your inventory. There are 3 durations:

- **Permanent** perks remain in effect until the perk is removed from your inventory.
- **Temporary** perks expire after a certain duration (usually after some number of hands or rounds).
- **Instant** perks are destroyed immediately after they're used.
  
#### Perk Modes

The mode indicates how the perk is activated. There are 2 modes:

- **Active** perks apply their modifications when activated by the player.
- **Passive** perks apply their modifications automatically when some condition is met.

#### Perk Rarities

The rarity indicates how impactful the perk is, and how likely you are to start with it or find it in the shop. The rarer a perk is, the more impactful it is to the game, and the harder it is to find. There are 4 rarities:

- **Common** perks have a %70 chance of appearing, and have 1 modifier
- **Uncommon** perks have a %20 chance of appearing, and have 2 modifiers
- **Rare** perks have a %12 chance of appearing, and have 3 modifiers
- **Legendary** perks have a %3 chance of appearing, and have 4 modifiers

#### Perk Editions

The edition indicates how many additional modifications a perk has. There are 3 editions:

- **Standard** edition perks have 0 additional modifications
- **Holographic** edition perks have 1 additional modification
- **Polychrome** edition perks have 2 additional modifications

### Money

You start each run with a small amount of money in your wallet. Money is added to your wallet after you play each hand that scores more than 0 points. Perks can add money to your wallet and take money out of it. You can sell perks in your inventory at any time. Money is spent in the shop.

### Shop

At the end of every 5 hands, the game pauses and the shop opens. The shop shows 2 random perks of each type, 3 random dice for purchase, and all scorecard categories available for purchase or upgrade. The shop can be re-stocked with a new set of random perks for a cost. You can buy any or all the contents of the shop, if you have enough money and enough space in your inventory. You can also choose to close the shop without spending any money. Once you close the shop, it won't be available again for another 5 hands.

## Gameplay

A run of Frigate consists of 15 rounds, with a variable number of hands in each round. You keep playing hands until you've either played every category of hand on your scorecard, or your round score matches or exceeds the round's score target -- whichever comes first. You win the round if your score meets or exceeds the score target. You lose the run if your score is less than the score target after playing every hand on your scorecard. Win the run by winning 15 rounds.

### Game Board

There are 6 areas of the game board:

- Run & Hand Details
- Scorecard
- Perk inventory
- Dice collection
- Throwing tray
- Queue

### Playing Hands

Each hand consists of two phases: rolling and scoring.

The starting hand size is 5 dice. It can be reduced to a minimum of 2 dice, and increased to a maximum of 8 dice. A full hand must be played every hand. So if the hand size is 5, then 5 dice must be played every hand. And if the hand size is 8, then 8 dice must be played every hand.

#### Rolling Phase

Each hand begins with the rolling phase:

1. Select N dice from your collection for this hand, where N is the current hand size, and place them in the tray
2. Roll all the dice in the tray to determine your hand
3. Move any dice you want to keep into the queue
4. Re-roll any dice you leave in the tray
5. Repeat steps 2-3 until no re-rolls remain, or all the dice are queued to play
6. Select an available scoring box to play your hand in
7. Play your hand
8. Go to the scoring phase

Perks can be sold, and active perks can be triggered, at any time during the rolling phase.

You must enter a hand into a scoring box on your scorecard every round. The scorng box in each category can only be filled in once per round (unless modified by a perk).

#### Scoring Phase

Each hand ends with the scoring phase. The scoring happens automatically in the order listed below:

1. Apply any perks that modify the category bonus
2. Apply any perks that modify the category multiplier
3. For each die in the queue from left to right:
   1. Apply any modifiers on the die face
   2. Add the face value to the category score box
4. Add the bonus to the score box
5. Multiply the value in the score box by the multiplier - this is your hand score
6. Apply any perks that modify your hand score
7. Add your hand score to your round score
8. Apply any perks that modify the category reward
9. Add category reward amount to your wallet

### Playing Rounds

A round ends when there are no more playable categories on your scorecard, or your total round score is equal to or greater than the round's score target.

If there are no more available categories, and your total round score is less than the score target, then the run ends and you lose. Otherwise you win the round, then all the scoring boxes on your scorecard are emptied, and the next round begins.

When you win round 15, you win the run, and can choose to continue playing in "endless" mode.

### Boss Rounds

Rounds 5, 10, and 15 are boss rounds. These boss rounds apply a random debuff to all hands in the round. The pool of available debuffs is different for each boss round. So any debuff that appears in round 5 will never appear in round 10 or 15.

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