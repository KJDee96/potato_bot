import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission

from bot import emoji_star
from bot.config import dataset, guild_ids, file
from bot.utils import store_data
from bot.user import find_user_by_discord_id, create_user_choices


class Star(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="check_potato",
                       description="Check potato star amount",
                       guild_ids=guild_ids,
                       options=[
                           create_option(
                               name="user",
                               description="Who to check.",
                               option_type=3,
                               required=True,
                               choices=create_user_choices(dataset)
                           ),
                       ])
    async def _check_potato(self, ctx: SlashContext, user: str):
        index, user = find_user_by_discord_id(dataset, int(user))
        await ctx.send(content=f"{user.name} has {user.stars} stars {emoji_star}")

    @cog_ext.cog_slash(name="give_potato",
                       description="Give potato star",
                       guild_ids=guild_ids,
                       options=[
                           create_option(
                               name="user",
                               description="Who to give the potato star to.",
                               option_type=3,
                               required=True,
                               choices=create_user_choices(dataset)
                           ),
                           create_option(
                               name="amount",
                               description="Amount of potato stars to give.",
                               option_type=4,
                               required=True
                           ),
                           create_option(
                               name="reason",
                               description="Reason for giving stars.",
                               option_type=3,
                               required=True
                           )
                       ])
    @cog_ext.permission(guild_id=guild_ids[0],
                        permissions=[
                            create_permission(815696612331749397, SlashCommandPermissionType.ROLE, True),
                        ])
    async def _give_potato(self, ctx: SlashContext, user: str, amount: int, reason: str):
        index, user = find_user_by_discord_id(dataset, int(user))
        user.stars += amount
        dataset[index] = user
        store_data(file, dataset)
        await ctx.send(
            content=f"{user.name} now has {user.stars} stars {emoji_star}\nThey were a good little potato for doing: {reason}")

    @cog_ext.cog_slash(name="take_away_potato",
                       description="Take away potato star",
                       guild_ids=guild_ids,
                       options=[
                           create_option(
                               name="user",
                               description="Who to take away the potato star from.",
                               option_type=3,
                               required=True,
                               choices=create_user_choices(dataset)
                           ),
                           create_option(
                               name="amount",
                               description="Amount of potato stars.txt to take away.",
                               option_type=4,
                               required=True
                           )
                       ])
    async def _take_away_potato(self, ctx: SlashContext, user: str, amount: int):
        index, user = find_user_by_discord_id(dataset, int(user))
        user.stars -= amount
        dataset[index] = user
        store_data(file, dataset)
        await ctx.send(content=f"{user.name} now has {user.stars} stars {emoji_star}")


def setup(bot):
    bot.add_cog(Star(bot))
