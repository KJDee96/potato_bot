from discord_slash.utils.manage_commands import create_choice


class User:
    def __init__(self, name="", stars=0, user_id=0):
        self.name = name
        self.stars = stars
        self.user_id = user_id


def find_user_by_discord_id(users, discord_user_id):
    for index, user in enumerate(users):
        if user.user_id == discord_user_id:
            return index, user


def find_user_by_name(users, name):
    for index, user in enumerate(users):
        if user.name == name:
            return index, user


def create_user_choices(users):
    choice_list = []
    for _, user in enumerate(users):
        choice_list.append(
            create_choice(
                name=user.name,
                value=str(user.user_id)
            )
        )
    return choice_list
