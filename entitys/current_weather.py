from mongoengine import *


class Main(EmbeddedDocument):
    temp = IntField()
    temp_min = FloatField()
    temp_max = FloatField()
    pressure = FloatField()
    humidity = FloatField()


class Weather(EmbeddedDocument):
    id = IntField()
    main = StringField()
    description = StringField()
    icon = StringField()


class Clouds(EmbeddedDocument):
    all = IntField()


class Wind(EmbeddedDocument):
    speed = FloatField()
    deg = FloatField()


class Sys(EmbeddedDocument):
    country = StringField()
    id = IntField()
    sunrise = IntField()
    sunset = IntField()
    type = IntField()


class Rain(EmbeddedDocument):
    one_h = FloatField()
    three_h = FloatField()


class Snow(EmbeddedDocument):
    one_h = FloatField()
    three_h = FloatField()


class Coord(EmbeddedDocument):
    lat = FloatField()
    lon = FloatField()


class CurrentWeather(Document):
    base = StringField()
    clouds = EmbeddedDocumentField(Clouds)
    cod = IntField()
    coord = EmbeddedDocumentField(Coord)
    dt = IntField()
    id = StringField(primary_key=True)
    main = EmbeddedDocumentField(Main)
    name = StringField()
    rain = EmbeddedDocumentField(Rain)
    snow = EmbeddedDocumentField(Snow)
    sys = EmbeddedDocumentField(Sys)
    timezone = IntField()
    visibility = IntField()
    weather = EmbeddedDocumentListField(Weather)
    wind = EmbeddedDocumentField(Wind)
