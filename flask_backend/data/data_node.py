from flask_backend.data import weather_api as api
from flask_backend.data import weather_dao as dao
from datetime import datetime


"""10 min"""

delay_for_current_weather = 10*60

"""1 hour"""

delay_for_forecast_weather = 60*60


def get_current_weather(args):
    args = dict(args)
    if 'q' in args:
        now_dt = datetime.now()
        weather = dao.get_current_weather_by_city_or_none(args['q'])
        if weather is not None and weather.dt - now_dt.timestamp() < delay_for_current_weather:
            return weather
        else:
            weather = api.get_current_weather(args)
            upgrade_response(weather)
            weather['id'] = weather['name']

            return dao.save_current_weather(weather)
    else:
        return api.get_current_weather(args)


def get_forecast_weather(args):
    args = dict(args)
    if 'q' in args:
        now_dt = datetime.now()
        weather = dao.get_forecast_weather_by_city_or_none(args['q'])
        if weather is not None and weather.start_dt - now_dt.timestamp() < delay_for_forecast_weather:
            return weather
        else:
            weather = api.get_forecast_5d3h_weather(args)

            weathers = weather['list']
            for one_weather in weathers:
                upgrade_response(one_weather)

            weather['_id'] = weather['city']['name']
            weather['start_dt'] = weather['list'][0]['dt']

            return dao.save_forecast_weathers(weather)
    else:
        return api.get_forecast_5d3h_weather(args)


def upgrade_response(one_weather):
    if 'rain' in one_weather:
        rain = one_weather['rain']
        dic = {}
        if '3h' in one_weather['rain']:
            dic['three_h'] = rain['3h']
        if '1h' in one_weather['rain']:
            dic['one_h'] = rain['1h']
        one_weather['rain'] = dic

    if 'snow' in one_weather:
        rain = one_weather['snow']
        dic = {}
        if '3h' in one_weather['snow']:
            dic['three_h'] = rain['3h']
        if '1h' in one_weather['snow']:
            dic['one_h'] = rain['1h']
        one_weather['snow'] = dic

    return one_weather
