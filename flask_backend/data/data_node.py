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
        if weather is not None and now_dt.timestamp() - weather.dt < delay_for_current_weather:
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
        if weather is not None and now_dt.timestamp() - weather.start_dt < delay_for_forecast_weather:
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

    determine_clothes_set(one_weather)

    return one_weather


def determine_clothes_set(one_weather):
    if one_weather['main']['temp'] < 273.15 + 15:
        temp = one_weather['main']['temp_min']
    else:
        temp = one_weather['main']['temp']

    if one_weather['weather'][0]['main'] == 'Rain' and 273.15 + 0 < temp < 273.15 + 20:
        one_weather['clothes'] = {'icon_id': 'set9'}
    else:
        if temp > 273.15 + 30:
            one_weather['clothes'] = {'icon_id': 'set0'}
        elif temp > 273.15 + 20:
            one_weather['clothes'] = {'icon_id': 'set1'}
        elif temp > 273.15 + 15:
            one_weather['clothes'] = {'icon_id': 'set2'}
        elif temp > 273.15 + 10:
            one_weather['clothes'] = {'icon_id': 'set3'}
        elif temp > 273.15 + 5:
            one_weather['clothes'] = {'icon_id': 'set4'}
        elif temp > 273.15 + 0:
            one_weather['clothes'] = {'icon_id': 'set5'}
        elif temp > 273.15 - 5:
            one_weather['clothes'] = {'icon_id': 'set5'}
        elif temp > 273.15 - 10:
            one_weather['clothes'] = {'icon_id': 'set6'}
        elif temp > 273.15 - 20:
            one_weather['clothes'] = {'icon_id': 'set7'}
        elif temp < 273.15 - 20:
            one_weather['clothes'] = {'icon_id': 'set8'}

    return one_weather

