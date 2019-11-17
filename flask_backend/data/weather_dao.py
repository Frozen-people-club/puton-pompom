from flask_backend.entitys.forecast_weather import ForecastWeather, DoesNotExist
from flask_backend.entitys.current_weather import CurrentWeather, DoesNotExist


def get_current_weather_by_city_or_none(city):
    try:
        return CurrentWeather.objects(id=city).get()
    except DoesNotExist:
        return None


def get_forecast_weather_by_city_or_none(city):
    try:
        return ForecastWeather.objects(_id=city).get()
    except DoesNotExist:
        return None


def save_current_weather(current_response):
    weather_object = CurrentWeather(**current_response)
    weather_object.save()
    return weather_object



def save_forecast_weathers(forecast_response):
    weather_object = ForecastWeather(**forecast_response)
    weather_object.save()
    return weather_object
