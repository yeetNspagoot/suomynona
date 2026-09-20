import hikari
import lightbulb

from suomynona import config, extensions


def main() -> None:
    bot = hikari.GatewayBot(token=config.DISCORD_TOKEN, intents=hikari.Intents.ALL_UNPRIVILEGED)
    client = lightbulb.client_from_app(bot)

    @bot.listen(hikari.StartingEvent)
    async def on_starting(_: hikari.StartingEvent) -> None:

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
