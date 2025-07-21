# Manual

This manual explains how to play Frigate.

## Content

- [Manual](#manual)
  - [Content](#content)
  - [Objective](#objective)
  - [Components](#components)
    - [Scorecard](#scorecard)
    - [Dice](#dice)
    - [Perks](#perks)
      - [Perk Durations](#perk-durations)
      - [Perk Modes](#perk-modes)
      - [Perk Rarities](#perk-rarities)
    - [Currency](#currency)
    - [Shop](#shop)
  - [Gameplay](#gameplay)
    - [Setup](#setup)
    - [Playing Hands](#playing-hands)
      - [Rolling Phase](#rolling-phase)
      - [Scoring Phase](#scoring-phase)
    - [Playing Rounds](#playing-rounds)
  - [Unlocking Features](#unlocking-features)
    - [Perks](#perks-1)
    - [Difficulty Levels](#difficulty-levels)
      - [Level Scaling](#level-scaling)
      - [Debuffs](#debuffs)

## Objective

Win a game (run) of Frigate by winning 10 rounds. Win each round by playing Yahtzee-style dice hands until your score matches or exceeds the round's score target. Each round has a higher score target than the previous round.

## Components

You start each run with a scorecard, a set of five D6 dice, two random perks in an inventory that can hold 4 perks, and a small amount of starting currency. Perks modify almost every aspect of the game. After every 5 hands, a shop appears where you can spend currency to buy new perks and scorecard slots.

### Scorecard

You start with a base scorecard that has 15 slots. Each slot has a scoring calculation, a bonus, a multiplier, and a reward. Slots can be upgraded to increase their bonus, multiplier, and reward.

Additional slots become available to purchase in the shop when you have the dice needed to play those hands. For example, the "Eights" slot becomes available when your dice set includes at least one D8.

Look at [docs/slots.md](docs/slots.md) for an exhaustive list of all the possible scorecard slots and their details.

### Dice

You start with a set of 5 D6 dice. Perks can modify your set of dice by adding new dice and modifying existing dice. The available types of dice are D4, D6, D8, and D10. You can have a maximum of 8 dice in your set.

### Perks

Perks modify how the game works. There are 3 categories of perks: dice perks, inventory perks, and scorecard perks. And each perk modifies something about that game component.

- Dice
  - How many dice are in your set
  - What types of dice are in your set
  - The values on the faces of your dice
  - Modifiers applied to dice faces
- Inventory
  - How many perks you can hold in your inventory
  - How much it costs to buy certain perks
  - Modifiers triggered by buying or selling perks
- Scorecard
  - Number of times you can play a slot in a round
  - Upgrade a slot
  - Remove a slot
  - Modifier applied after calculating hand score

Each perk has a duration, mode, and rarity.

#### Perk Durations

The duration indicates how long the perk exists in your inventory. There are 3 durations:

- **Permanent** perks remain in effect until the perk is sold
- **Temporary** perks expire after a certain duration (usually after some number of rounds)
- **One-time** perks are destroyed immediately after they're used
  
#### Perk Modes

The mode indicates how the perk is activated. There are 2 modes:

- **Active** perks apply their modifications when manually triggered by the player
- **Passive** perks apply their modifications automatically when some condition is met

#### Perk Rarities

The rarity indicates how impactful the perk is, and how likely you are to start with it or find it in the shop. The rarer a perk is, the more impactful it is to the game and the harder it is to find. There are 4 rarities:

- **Common**
- **Uncommon**
- **Rare**
- **Legendary**

### Currency

You start each run with a small amount of starting currency. You gain some amount of currency after each hand that scores more than 0 points.

### Shop

The shop opens at the end of every 5 rounds. The shop shows 2 random perks from each category, and all available scorecard slots. The shop can be re-stocked with a new set of perks for a cost.

## Gameplay

A run of Frigate consists of 10 rounds, with a variable number of hands in each round. You keep playing hands until you've either filled all the slots on your scorecard, or your score matches or exceeds the round's score target -- whichever comes first. You win the round if your score meets or exceeds the score target. You lose the round if your score is less than the score target after playing every hand on your scorecard.

### Setup

Start round 1 hand 1 with the following:

* A scorecard
* A set of five D6 dice
* Two random perks in an inventory that holds 4 perks
* A small amount of starting currency

### Playing Hands

Each hand consists of two phases: rolling and scoring.

#### Rolling Phase

Each hand begins with the rolling phase. You must enter a hand into a slot on your scorecard by the end of the rolling phase. Each slot can only be filled once per round (unless modified by a perk).

1. Roll all your dice to determine your hand
2. Choose either to play your hand, or re-roll one or more of your dice
3. If you choose to play your hand:
   1. Select the slot to place your hand in on your scorecard
   2. Go to the scoring phase
4. If you choose to re-roll:
   1. Set aside any dice you want to keep
   2. Re-roll the remaining dice
   3. Re-roll up to 2 times
   4. Select the slot to place your hand in on your scorecard
   5. Go to the scoring phase

Perks can be sold, and active perks can be triggered, at any time during the rolling phase.

#### Scoring Phase

Each hand ends with the scoring phase. Scoring happens automatically after playing your hand in the rolling phase. This is the scoring process:

1. Apply any perks that modify the slot's bonus
2. Apply any perks that modify the slot's multiplier
3. Perform the scoring calculation on the hand (sum)
4. Add the bonus to this sum
5. Multiply the result by the multiplier to get the total hand score
6. Apply any perks that modify the total hand score
7. Add the total hand score to your total round score
8. Apply any perks that modify the slot's reward
9. Add any earned currency to your "wallet"

Perks can modify the base score, multiplier, or reward of a scorecard slot, either permanently or while the perk is active.

- *For example, a perk for the "Aces" slot can add +5 bonus points, or increase its multiplier to 3x.*

Perks can modify your total hand score.

- *For example, after calculating summing your dice, adding bonus points, and multiplying the result, the resulting score can be further multiplied by 2x.*

### Playing Rounds

A round ends when there are no more playable slots on your scorecard, or your total round score is equal to or greater than the round's score target.

If there are no more open slots and your total round score is less than the score target, then you lose the run. Otherwise, you win the round and progress to the next round.

When you win a round, all the slots on your scorecard are emptied, and the next round begins.

When you win round 10, you win the run, and can optionally continue playing in "endless" mode.

## Unlocking Features

### Perks

Not all perks are immediately available. Some perks need to be unlocked by achieving certain accomplishments in the game. Look at [docs/perks.md](docs/perks.md) to see which perks need to be unlocked, and what the unlock criteria are.

### Difficulty Levels

You can choose the game difficulty when starting a new run. Only one difficulty level is available at the start.

Once you win your first run, you can play runs at a higher difficulty level. Once you win a run at that difficulty level, you unlock an even higher level, and so-on.

As you progress through difficulty levels, the score targets get higher, and debuffs start getting applied.

#### Level Scaling

The score target of each round is calculated using a scaling function. Each level up in difficulty changes this scaling function so that the target scores for each round get larger sooner in the run.

**The scaling function is TBD and will be worked out through trial and error during development.**

*Add description of scaling function here once determined*

#### Debuffs

Higher difficulty levels also have debuffs that apply for the whole run. *For example, all scorescard slots give -1 bonus and -1 multiplier.*

**Debuffs are TBD and will be worked out through trial and error during development.**

*Add description or table of debuffs here once determined*