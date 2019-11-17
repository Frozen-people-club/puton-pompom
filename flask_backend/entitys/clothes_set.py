from mongoengine import *


class ClothesSet(EmbeddedDocument):
    icon_id = StringField()
