# Frigate

Frigate is a Yahtzee-themed roguelike deckbuilding game inspired by Balatro.

## Goal

Win a game (run) of frigate by winning 10 rounds. Win each round by playing Yahtzee-style dice hands until your score matches or exceeds the round's score target. Each round has a higher score target than the previous round.

## Components

You start each run with a scorecard, a set of five D6 dice, two random perks in an inventory that can hold 4 perks, and a small amount of starting currency. Perks modify almost every aspect of the game. After every 5 hands, a shop appears where you can spend money to buy new perks. Perks in your inventory can be sold at any time.

### Scorecard

You start with a base scorecard that has 15 slots. Each slot has a scoring calculation, a bonus, and a multiplier:

| Slot | Calculation | Bonus | Multiplier | Currency Earned |
| --- | --- | --- | --- | --- |
| Aces | Sum of all dice with 1 | +0 | x1 | $1 |
| Twos | Sum of all dice with 2 | +0 | x1 | $1 |
| Threes | Sum of all dice with 3 | +0 | x1 | $1 |
| Fours | Sum of all dice with 4 | +0 | x1 | $1 |
| Fives | Sum of all dice with 5 | +0 | x1 | $1 |
| Sixes | Sum of all dice with 6 | +0 | x1 | $1 |
| Wild | Sum of all dice | +0 | x1 | $1 |
| Pair | Sum of the 2 paired dice | +2 | x1 | $1 |
| Two Pair | Sum of the 4 dice | +2 | x1 | $1 |
| Full House | Sum of all 5 dice | +2 | x1 | $1 |
| Small Straight | Sum of the 4 consecutive dice | +2 | x1 | $1 |
| Large Straight | Sum of all 5 consecutive dice | +2 | x1 | $1 |
| Three of a Kind | Sum of the 3 dice | +2 | x1 | $1 |
| Four of a Kind | Sum of the 4 dice | +2 | x1 | $1 |
| Five of a Kind | Sum of the 5 dice | +2 | x1 | $1 |

Additional slots become available on your scorecard automatically when you have the dice and/or perks needed to play those hands. For example, the "Eights" slot is added to your scorecard when your dice set includes at least one D8.

### Dice

You start with a set of 5 D6 dice. In addition to D6, these 5 other types of dice are available via perks:

- D4
- D8
- D10
- D12
- D20

### Perks

Perks modify how the game works. There are 3 categories of perks: dice perks, inventory perks, and scorecard perks. And each perk modifies something about that game component.

- Dice
  - How many dice are in your set
  - What kinds of dice are in your set
  - The values on the faces of your dice
  - Score modifiers applied to dice faces
- Inventory
  - How many perks you can hold in your inventory
  - How much it costs to buy certain perks
  - Score modifiers triggered by buying or selling perks
- Scorecard
  - Number of times you can play a slot in a round
  - Slot bonus
  - Slot multiplier
  - Score modifiers applied to the final score of your hand
  - How much currency you earn when scoring a slot

Each perk has a duration and a mode.

#### Perk Durations

There are 3 perk durations:

- **Permanent** perks remain in effect until the perk is sold
- **Temporary** perks expire after a certain duration (usually after some number of rounds)
- **One-time** perks are destroyed immediately after they're used
  
#### Perk Modes

There are 2 perk modes:

- **Active** perks apply their modifications when manually triggered by the player
- **Passive** perks apply their modifications automatically when some condition is met

### Currency

You start each run with a small amount of starting currency. You gain some amount of currency after each hand that scores more than 0 points.

### Shop

The shop opens at the end of every 5 rounds. The shop shows 2 random perks from each category. The shop can be re-stocked with a new set of perks for a cost.

## Gameplay

A run of frigate consists of 10 rounds with a variable number of hands. You keep playing hands until you've either scored all the hands on your scorecard, or your score matches or exceeds the round's score target -- whichever comes first. You win if your score meets or exceeds the score target. You lose if your score is less than the score target after playing every hand on your scorecard.

### Setup

Start round 1 hand 1 with the following:

* A scorecard
* A set of five D6 dice
* Two random perks in an inventory that can hold 4 perks
* A small amount of starting currency

### Playing Hands

Each hand consists of two phases: rolling and scoring.

#### Rolling Phase

A hand begins with the rolling phase. Perks can be sold, and active perks can be triggered, at any time during the rolling phase. You must enter a hand into a slot on your scorecard by the end of the rolling phase. Each slot can only be played once per round.

1. Roll all your dice to determine your hand
2. Choose either to play your hand, or re-roll one or more of your dice
3. If you choose to play your hand:
   1. Play your hand by selecting a slot on your scorecard
   2. Go to the scoring phase
4. If you choose to re-roll:
   1. Set aside any dice you want to keep
   2. Re-roll the remaining dice
   3. Re-roll up to 2 times
   4. Play your hand by selecting a slot on your scorcard
   5. Go to the scoring phase

#### Scoring Phase

A hand ends with the scoring phase.

Perks can modify the base score or the base multiplier of a scorecard slot, either permanently or while the perk is active.

- *For example, a perk for the "Aces" slot can add +5 to the sum, or increase its multiplier to 3x. This upgrade can either be permanent or only in effect while the perk is in your inventory.*

Perks can also modify the final score of a scorecard slot.

- *For example, after calculating the score times the multiplier, the resulting score can be further multiplied by 2x.*

Scoring happens automatically after playing your hand in the rolling phase:

1. Apply any perks that modify the slot's base bonus
2. Apply any perks that modify the slot's base multiplier
3. Perform the scoring calculation (sum)
4. Add the bonus to this sum
5. Multiply the result by the multiplier to get the final score for your hand
6. Apply any perks that modify the final score of your hand
7. Add the final score to your total round score
8. Apply any perks that modify the currency earned
9. Add any earned currency to your "wallet"

### Playing Rounds

A round ends when there are no more playable slots on your scorecard, or your total round score is equal to or greater than the score target.

If there are no more playable slots and your total round score is less than the score target, then you lose the run. Otherwise, you win the round and progress to the next round.

When you win a round, all the slots on your scorecard are emptied, and the next round begins.

When you win round 10, you win the run, and can optionally continue playing in "endless" mode.
