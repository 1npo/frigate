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
    - [Money](#money)
    - [Shop](#shop)
  - [Gameplay](#gameplay)
    - [Game Board](#game-board)
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

You start each run with a scorecard, a set of five D6 dice, two random perks in an inventory that can hold 5 perks, and a wallet containing a small amount of starting money. Perks modify almost every aspect of the game. After every 5 hands, a shop appears where you can spend money to buy new perks and scorecard categories.

### Scorecard

You start with a base scorecard that has 15 hand categories. Each category has a scoring calculation, a bonus, a multiplier, a reward, and a scoring box. Categories can be upgraded to permanently increase their bonus, multiplier, and reward.

Additional hand categories become available to purchase in the shop when you have the dice needed to play those hands. For example, the "Eights" category becomes available when your dice set includes at least one D8. See [categories.md](categories.md) for an exhaustive list of all categories and their details.

### Dice

You start with a set of 5 D6 dice. Perks enable you to change the type of dice in your hand and add new dice to your hand. The available types of dice are D4, D6, D8, and D10. You can have a maximum of 8 dice in your set.

### Perks

Perks modify how the game works. There are 3 types of perks: dice perks, scorecard perks, and inventory perks. Each perk modifies something about that game component, and has a duration, mode, and rarity. See [perks.md](perks.md) for an exhaustive list of all perks and their details.

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

- **Common**
- **Uncommon**
- **Rare**
- **Legendary**

### Money

You start each run with a small amount of money in your wallet. Money is added to your wallet after you play each hand that scores more than 0 points. Perks can add money to your wallet and take money out of it. You can sell perks in your inventory at any time. Money is spent in the shop.

### Shop

At the end of every 5 hands, the game pauses and the shop opens. The shop shows 2 random perks of each type, and all available scorecard categories. The shop can be re-stocked with a new set of random perks for a cost. You can buy any or all the contents of the shop, if you have enough money and enough space in your inventory. You can also choose to close the shop without spending any money. Once you close the shop, it won't be available again for another 5 hands.

## Gameplay

A run of Frigate consists of 10 rounds, with a variable number of hands in each round. You keep playing hands until you've either played every category of hand on your scorecard, or your round score matches or exceeds the round's score target -- whichever comes first. You win the round if your score meets or exceeds the score target. You lose the run if your score is less than the score target after playing every hand on your scorecard. Win the run by winning 10 rounds.

### Game Board

The game board consists of a tray and a queue. The tray is where you roll your dice in each hand. The queue is where you arrange your dice to be played as a hand.

### Playing Hands

Each hand consists of two phases: rolling and scoring.

#### Rolling Phase

Each hand begins with the rolling phase:

1. Roll all your dice in your tray to determine your hand
2. Move any dice you want to keep into your queue
3. Re-roll any dice you leave in your tray
4. Repeat steps 2-3 until no re-rolls remain, or all your dice are queued to play
5. Select an available scoring box to play your hand in
6. Play your hand
7. Go to the scoring phase

Perks can be sold, and active perks can be triggered, at any time during the rolling phase.

You must enter a hand into a scoring box on your scorecard every round. The scorng box in each category can only be filled in once per round (unless modified by a perk).

#### Scoring Phase

Each hand ends with the scoring phase, and the scoring happens automatically in this order:

1. Apply any perks that modify the category bonus
2. Apply any perks that modify the category multiplier
3. Perform the scoring calculation on the hand (sum)
4. Add the bonus to this sum
5. Multiply the summation by the multiplier to get your hand score
6. Apply any perks that modify your hand score
7. Add your hand score to your round score
8. Apply any perks that modify the category reward
9. Add any earned money to your wallet

### Playing Rounds

A round ends when there are no more playable categories on your scorecard, or your total round score is equal to or greater than the round's score target.

If there are no more available categories and your total round score is less than the score target, then the run ends and you lose. Otherwise, you win the round. Then all the scoring boxes on your scorecard are emptied, and the next round begins.

When you win round 10, you win the run, and can choose to continue playing in "endless" mode.

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