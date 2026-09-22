import aiosqlite
import hikari
import lightbulb

from suomynona import config
from suomynona.utils import database, messages

loader = lightbulb.Loader()

LOG_TYPES = [
    lightbulb.Choice(
        "Placeholder Type", database.GuildSettingKey.PLACEHOLDER_SETTING_NAME.value
    ),
]


@loader.command
class SetLogChannelCommand(
    lightbulb.SlashCommand,
    name="set_log_channel",
    description="Sets the current channel as a log channel.",
    default_member_permissions=hikari.Permissions.MANAGE_GUILD,
    contexts=[hikari.ApplicationContextType.GUILD],
):
    log_type = lightbulb.string(
        "log_type", "The type of events to log.", choices=LOG_TYPES
    )

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context, db: aiosqlite.Connection) -> None:
        if ctx.guild_id is None:
            response = messages.build_response(
                content="This command can only be used in a server.",
                accent_colour=config.ERROR_COLOUR,
            )
            await ctx.respond(components=response)
            return

        setting_key = database.GuildSettingKey(self.log_type)
        current_channel_id = await database.get_guild_setting(
            db, ctx.guild_id, setting_key
        )

        log_type_name = self.log_type.replace("_", " ").title()

        if current_channel_id == ctx.channel_id:
            response = messages.build_response(
                content=f"This channel is already set as the log channel for **{log_type_name}**.",
                accent_colour=config.ERROR_COLOUR,
            )
            await ctx.respond(components=response)
            return

        await database.set_guild_setting(db, ctx.guild_id, setting_key, ctx.channel_id)

        if current_channel_id is None:
            content = f"Set this channel (<#{ctx.channel_id}>) as the log channel for **{log_type_name}**."
        else:
            content = f"Changed the **{log_type_name}** log channel from <#{current_channel_id}> to <#{ctx.channel_id}>."

        response = messages.build_response(content=content)
        await ctx.respond(components=response)
