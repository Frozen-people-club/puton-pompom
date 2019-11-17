import requests
import json

open_weather_url = 'http://api.openweathermap.org/data/2.5/'
open_weather_app_id = 'e701799ce287e27435705e293e56f97c'


def get_current_weather(args):
    args['APPID'] = open_weather_app_id
    url = open_weather_url + "weather"
    return __do_request(url, args)


def get_forecast_5d3h_weather(args):
    args['APPID'] = open_weather_app_id
    url = open_weather_url + "forecast"
    return __do_request(url, args)


def __do_request(url, args):
    request = requests.get(url, params=args)
    response = {
        'error': 'weather api error'
    }
    if request.ok:
        response = json.loads(request.content)
    else:
        request.raise_for_status()
    return response
