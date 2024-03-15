from pymongo import MongoClient

import config

ROSSYdb = MongoClient(config.MONGO_URL)
ROSSY = ROSSYdb["ROSSYDb"]["ROSSY"]


from .chats import *
from .users import *
