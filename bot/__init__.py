from pathlib import Path
from discord.ext import commands
from discord_slash import SlashCommand
from bot.config import token

bot = commands.Bot(command_prefix=";")
slash = SlashCommand(bot, sync_commands=True)  # Declares slash commands through the client.

emoji_star = '<:star:869923498410250320>'


def extensions():
    files = Path("bot", "cogs").rglob("*.py")
    for file in files:
        yield file.as_posix()[:-3].replace("/", ".")


def load_extensions(_bot):
    for ext in extensions():
        try:
            _bot.load_extension(ext)
            print(f'Loaded {ext}')
        except Exception as ex:
            print(f"Failed to load extension {ext} - exception: {ex}")


@bot.event
async def on_ready():
    print("Ready!")


def run():
    load_extensions(bot)
    bot.run(config.token)
