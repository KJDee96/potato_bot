import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from bot import emoji_star
from bot.config import guild_ids


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test",
                       guild_ids=guild_ids,
                       description="test")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="embed test")
        await ctx.send(content="test", embeds=[embed])

    @cog_ext.cog_slash(name="say",
                       guild_ids=guild_ids,
                       description="Potato say.",
                       options=[
                           create_option(
                               name="sentence",
                               description="What potato bot should say.",
                               option_type=3,
                               required=True
                           )
                       ])
    async def _say(self, ctx: SlashContext, sentence: str):
        await ctx.send(content=f"Potato say {sentence} {emoji_star}!")


def setup(bot):
    bot.add_cog(Test(bot))
