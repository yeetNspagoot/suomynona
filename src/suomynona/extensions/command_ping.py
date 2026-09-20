import lightbulb

from suomynona.utils import messages

loader = lightbulb.Loader()


@loader.command
class PingCommand(lightbulb.SlashCommand, name="ping", description="Checks if the bot is alive or not."):

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        response = messages.build_response(content="Pong!")
        await ctx.respond(components=response)
