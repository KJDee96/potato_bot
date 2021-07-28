import discord
from discord_slash import SlashCommand  # Importing the newly installed library.
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
import pickle
from user import User

file = 'stars.data'

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)  # Declares slash commands through the client.

guild_ids = [815668740322361384]  # Put your server ID in this array.


def find_user(users, discord_user_id):
    for index, item in enumerate(users):
        if item.user_id == discord_user_id:
            return index, item


def store_data(data):
    with open(file, 'wb') as fw:
        pickle.dump(data, fw)
        fw.close()


def load_data():
    with open(file, 'rb') as fd:
        return pickle.load(fd)


dataset = load_data()


@slash.slash(name="say",
             guild_ids=guild_ids,
             description="Potato say.",
             options=[
                 create_option(
                     name="optone",
                     description="This is the first option we have.",
                     option_type=3,
                     required=False
                 )
             ])
async def _say(ctx, optone: str):
    await ctx.send(content=f"Potato say {optone} <:star:869923498410250320>!")


@slash.slash(name="check_potato",
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
async def _check_potato(ctx, user: str):
    index, user = find_user(dataset, int(user))
    await ctx.send(content=f"{user.name} has {user.stars} stars <:star:869923498410250320>")


@slash.slash(name="give_potato",
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
async def _give_potato(ctx, user: str, amount: int):
    index, user = find_user(dataset, int(user))
    user.stars += amount
    dataset[index] = user
    store_data(dataset)
    await ctx.send(content=f"{user.name} now has {user.stars} stars <:star:869923498410250320>")


@slash.slash(name="take_away_potato",
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
@slash.permission(guild_id=815668740322361384,
                  permissions=[
                      create_permission(88888888, SlashCommandPermissionType.USER, True)
                  ])
async def _take_away_potato(ctx, user: str, amount: int):
    index, user = find_user(dataset, int(user))
    user.stars -= amount
    dataset[index] = user
    store_data(dataset)
    await ctx.send(content=f"{user.name} now has {user.stars} stars <:star:869923498410250320>")


@client.event
async def on_ready():
    print("Ready!")


client.run("ODcwMDQ0Mjg1NTMyMjYyNDIw.YQHB4g.RXDCPFBVGnFQRREocdNvkhZNuWU")
