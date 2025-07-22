## What to Contribute

- Report bugs
- Request enhancements or changes
- Submit pull requests to fix bugs
- Submit pull requests to implement enhancements or changes

## How to Contribute

### Clone the repository

```bash
git clone https://github.com/1npo/frigate.git
cd frigate
```

### Install `uv`

#### via `curl`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via [some other method](https://docs.astral.sh/uv/getting-started/installation/)

### Install pre-commit hooks

```bash
uvx pre-commit install
```

### Set up a virtual environment and install dependencies

```bash
uv sync
```

### Set up a `.env` file (***Placeholder***)

**TODO**: Start using `dotenv` to manage defaults / other constants

## Running Tests

```bash
uvx coverage run -m pytest
```

## Submitting a Pull Request

1. Check out a feature branch: `git checkout -b feature-name`
2. Make your changes on this feature branch
3. Make atomic commits with clear commit messages
4. Push your commits to the feature branch
5. Create a PR to merge the feature branch into `main`
6. When the PR is approved, update your cloned repo: `git checkout main; git pull origin main`

