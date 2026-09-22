import aiosqlite
import hikari
import lightbulb

from suomynona import config, extensions
from suomynona.utils import database


def main() -> None:
    bot = hikari.GatewayBot(
        token=config.DISCORD_TOKEN, intents=hikari.Intents.ALL_UNPRIVILEGED
    )
    client = lightbulb.client_from_app(bot)

    @bot.listen(hikari.StartingEvent)
    async def on_starting(_: hikari.StartingEvent) -> None:

        # Register the db as a dependency so we can use it everywhere.
        db = await database.open_database()
        client.di.registry_for(lightbulb.di.Contexts.DEFAULT).register_value(
            aiosqlite.Connection,
            db,
            teardown=aiosqlite.Connection.close,
        )

        await client.load_extensions_from_package(extensions, recursive=True)
        await client.start()

    @bot.listen(hikari.StoppingEvent)
    async def on_stopping(_: hikari.StoppingEvent) -> None:
        await client.stop()

    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="In Development!",
            type=hikari.ActivityType.CUSTOM,
        ),
    )


if __name__ == "__main__":
    main()
