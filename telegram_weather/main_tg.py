import telebot
import requests
import datetime
from config import token, open_weather_api

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!\nЧтобы получить прогноз погоды, введи название города!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_api}&units=metric&lang=ru')
        data = r.json()
        city = data['name']
        current_weather = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        time = datetime.datetime.now().replace(microsecond=0)
        bot.send_message(message.chat.id, f'------{time}------\nПогода в городе: {city}\nТемпература: {current_weather} C°\n'
        f'Влажность: {humidity} %\nСкорость ветра: {wind} м/с')
    except:
        bot.send_message(message.chat.id, 'Проверьте название города!')


if __name__ == '__main__':
    bot.polling()
