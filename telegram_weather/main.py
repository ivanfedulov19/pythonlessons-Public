import requests
import datetime
from pprint import pprint
from config import token, open_weather_api

def get_weather(city,open_weather_api):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_api}&units=metric&lang=ru')
        data = r.json()
        pprint(data)
        city = data['name']
        current_weather = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        time = datetime.datetime.now().replace(microsecond=0)
        print(f'------{time}------\nПогода в городе: {city}\nТемпература: {current_weather} C°\n'
        f'Влажность: {humidity} %\nСкорость ветра: {wind} м/с')
    except Exception as ex:
        print(ex)
        print('Проверьте название города!')

def main():
    city = input('Введите город: ')
    get_weather(city,open_weather_api)


if __name__ == '__main__':
    main()
















