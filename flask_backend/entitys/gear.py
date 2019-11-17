from mongoengine import *


class Gear(Document):
    prefer_temp = IntField(min_value=273.15 - 50, max_value=273.15 + 50)
    is_purged = BooleanField()
    is_wetable = BooleanField()
