import requests


def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}\
            &units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    data_json = requests.get(url).json()
    return data_json
