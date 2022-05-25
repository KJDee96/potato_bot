from pathlib import Path

from bot.utils import load_data
import os

project_path = Path(__file__).parent.parent
file = os.path.join(project_path, 'stars.data')
guild_ids = [815668740322361384]
dataset = load_data(file)
token = ""