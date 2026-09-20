from enum import StrEnum
from pathlib import Path

import aiosqlite

from suomynona import config


class GuildSettingKey(StrEnum):
    """Keys used to identify guild settings in the database."""

    # Placeholder for now, update with moderation etc as things get added.
    PLACEHOLDER_SETTING_NAME = "placeholder_setting_name"


async def open_database() -> aiosqlite.Connection:
    Path(config.DB_PATH).parent.mkdir(parents=True, exist_ok=True)

    db = await aiosqlite.connect(config.DB_PATH)
    db.row_factory = aiosqlite.Row

    try:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS guild_settings(
            guild_id INTEGER NOT NULL,
            setting_key TEXT NOT NULL,
            setting_value INTEGER NOT NULL,
            PRIMARY KEY (guild_id, setting_key)
            );
            """
        )
        await db.commit()
    except Exception:
        await db.close()
        raise

    return db


async def set_guild_setting(db: aiosqlite.Connection, guild_id: int, setting_key: GuildSettingKey, setting_value: int) -> None:
    await db.execute(
        """
        INSERT INTO guild_settings (guild_id, setting_key, setting_value)
        VALUES (?, ?, ?)
        ON CONFLICT(guild_id, setting_key) DO UPDATE SET setting_value = excluded.setting_value
        """, (guild_id, setting_key, setting_value)
    )
    await db.commit()


async def remove_guild_setting(db: aiosqlite.Connection, guild_id: int, setting_key: GuildSettingKey) -> None:
    await db.execute(
        """
        DELETE FROM guild_settings WHERE guild_id = ? AND setting_key = ?
        """, (guild_id, setting_key)
    )
    await db.commit()
