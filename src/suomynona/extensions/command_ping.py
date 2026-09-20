import lightbulb

loader = lightbulb.Loader()


@loader.command
class PingCommand(lightbulb.SlashCommand, name="ping", description="Checks if the bot is alive or not."):

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond("Pong!")