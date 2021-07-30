import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission

from bot.config import dataset, guild_ids, file
from bot.utils import find_user, store_data


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
                               choices=[
                                   create_choice(
                                       name="Cerys",
                                       value="175255906056011788"
                                   ),
                                   create_choice(
                                       name="Emily",
                                       value="208189163382505473"
                                   ),
                                   create_choice(
                                       name="Jon",
                                       value="444910722187657216"
                                   )
                               ]
                           ),
                       ])
    async def _check_potato(self, ctx: SlashContext, user: str):
        index, user = find_user(dataset, int(user))
        await ctx.send(content=f"{user.name} has {user.stars} stars <:star:869923498410250320>")

    @cog_ext.cog_slash(name="give_potato",
                       description="Give potato star",
                       guild_ids=guild_ids,
                       options=[
                           create_option(
                               name="user",
                               description="Who to give the potato star to.",
                               option_type=3,
                               required=True,
                               choices=[
                                   create_choice(
                                       name="Cerys",
                                       value="175255906056011788"
                                   ),
                                   create_choice(
                                       name="Emily",
                                       value="208189163382505473"
                                   ),
                                   create_choice(
                                       name="Jon",
                                       value="444910722187657216"
                                   )
                               ]
                           ),
                           create_option(
                               name="amount",
                               description="Amount of potato stars.txt to give.",
                               option_type=4,
                               required=True
                           )

                       ])
    async def _give_potato(self, ctx: SlashContext, user: str, amount: int):
        index, user = find_user(dataset, int(user))
        user.stars += amount
        dataset[index] = user
        store_data(file, dataset)
        await ctx.send(content=f"{user.name} now has {user.stars} stars <:star:869923498410250320>")

    @cog_ext.cog_slash(name="take_away_potato",
                       description="Take away potato star",
                       guild_ids=guild_ids,
                       options=[
                           create_option(
                               name="user",
                               description="Who to take away the potato star from.",
                               option_type=3,
                               required=True,
                               choices=[
                                   create_choice(
                                       name="Cerys",
                                       value="175255906056011788"
                                   ),
                                   create_choice(
                                       name="Emily",
                                       value="208189163382505473"
                                   ),
                                   create_choice(
                                       name="Jon",
                                       value="444910722187657216"
                                   )
                               ]
                           ),
                           create_option(
                               name="amount",
                               description="Amount of potato stars.txt to take away.",
                               option_type=4,
                               required=True
                           )

                       ])
    @cog_ext.permission(guild_id=815668740322361384,
                        permissions=[
                            create_permission(88888888, SlashCommandPermissionType.USER, True)
                        ])
    async def _take_away_potato(self, ctx: SlashContext, user: str, amount: int):
        index, user = find_user(dataset, int(user))
        user.stars -= amount
        dataset[index] = user
        store_data(file, dataset)
        await ctx.send(content=f"{user.name} now has {user.stars} stars <:star:869923498410250320>")


def setup(bot):
    bot.add_cog(Star(bot))
