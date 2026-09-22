import os

import hikari
from dotenv import load_dotenv

load_dotenv()


# Environment
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

# Bot
DEFAULT_COLOUR = hikari.Colour(0x4A2C4C)
ERROR_COLOUR = hikari.Colour(0xFF0000)

# Paths
DB_PATH = "data/suomynona.db"
