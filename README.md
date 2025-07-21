# Frigate

A Yahtzee-themed roguelike deckbuilding game inspired by Balatro

>[!NOTE]
> This is a proof-of-concept. It's written in Python with Textual for the user interface, because I write Python for a living and Textual is the only GUI framework I'm familiar with. It's runs in a terminal, or can be run as a web server and played in your browser. This isn't an optimal user experience for a game.
> 
> Writing this POC will let me flesh out the idea, fix issues with balancing and synergies, and figure out an optimal application design. If it ends up being fun and worth the effort, I plan to rewrite it in Kotlin with libGDX so it can run natively on desktop and mobile, and make it available in app stores.

## Contents

- [Frigate](#frigate)
  - [Contents](#contents)
  - [How to Play](#how-to-play)
  - [Screenshots](#screenshots)
  - [Documentation](#documentation)
  - [Acknowledgements](#acknowledgements)
  - [Contributing](#contributing)

## How to Play

The preferred way to download and play Frigate is with `uvx`. These instructions assume you've already [installed `uv`](https://docs.astral.sh/uv/getting-started/installation/).

1. Open a terminal
2. Run `uvx frigate-game`
3. Play Frigate!

To run Frigate in web server mode:

1. Open a terminal
2. Run `uvx frigate-game --web --host 127.0.0.1 --port 8080`
3. Open [http://127.0.0.1:8080/](http://127.0.0.1:8080/) in your web browser
4. Play Frigate!

## Screenshots

*Add screenshots here when they become available*

## Documentation

- See [docs/manual.md](docs/manual.md) for the game's instruction manual
- See [docs/perks.md](docs/perks.md) for an exhaustive list of perks
- See [docs/slots.md](docs/slots.md) for an exhaustive list of scorecard slots

## Acknowledgements

- A huge thanks to [LocalThunk](https://x.com/localthunk) for creating [Balatro](https://www.playbalatro.com/), one of the greatest videogames of all time, and the inspiration for Frigate

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for what you can contribute and how to contribute. 