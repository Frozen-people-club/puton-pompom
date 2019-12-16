from mongoengine import *
from flask_backend.entitys.clothes_set import ClothesSet

class Main(EmbeddedDocument):
    temp = IntField()
    temp_min = FloatField()
    temp_max = FloatField()
    temp_kf = FloatField()
    feels_like = FloatField()
    pressure = FloatField()
    sea_level = FloatField()
    grnd_level = FloatField()
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
    pod = StringField()


class Rain(EmbeddedDocument):
    three_h = FloatField()


class Snow(EmbeddedDocument):
    three_h = FloatField()


class OneWeather(EmbeddedDocument):
    dt = IntField()
    dt_txt = StringField()
    main = EmbeddedDocumentField(Main)
    weather = EmbeddedDocumentListField(Weather)
    clouds = EmbeddedDocumentField(Clouds)
    wind = EmbeddedDocumentField(Wind)
    sys = EmbeddedDocumentField(Sys)
    rain = EmbeddedDocumentField(Rain)
    snow = EmbeddedDocumentField(Snow)
    clothes = EmbeddedDocumentField(ClothesSet)


class Coord(EmbeddedDocument):
    lat = FloatField()
    lon = FloatField()


class City(EmbeddedDocument):
    coord = EmbeddedDocumentField(Coord)
    country = StringField()
    id = IntField()
    name = StringField()
    population = IntField()
    sunrise = IntField()
    sunset = IntField()
    timezone = IntField()


class ForecastWeather(Document):
    _id = StringField(primary_key=True)
    city = EmbeddedDocumentField(City)
    start_dt = IntField()
    cnt = IntField()
    cod = IntField()
    list = EmbeddedDocumentListField(OneWeather)
    message = IntField()
