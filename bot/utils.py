import os
import pickle
from bot.user import User


def store_data(file, data):
    with open(file, 'wb') as fw:
        pickle.dump(data, fw)


def load_data(file):
    if not os.path.isfile(file):
        with open(file, 'wb+') as fw:
            emily = User("Emily", 38, 208189163382505473)
            cerys = User("Cerys", 60, 175255906056011788)
            jon = User("Jon", 15, 444910722187657216)
            pickle.dump([emily, cerys, jon], fw)
    with open(file, 'rb') as fd:
        return pickle.load(fd)
