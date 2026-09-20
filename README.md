# Suomynona
A Discord bot built with Hikari and Lightbulb, intended for server moderation and logging.

## Requirements
- Python 3.14+
- uv
- A Discord bot token

## Setup
1. Install dependencies:
   ```sh
   uv sync
   ```

2. Copy `.env.example` to `.env` and set `DISCORD_TOKEN` to your bot token.

3. Start the bot:
   ```sh
   uv run suomynona
   ```

## Commands
- `/ping` — Check whether the bot is responding.
