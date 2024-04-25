from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import requests
import datetime
from config import open_weather_token
import random
from aiogram.utils.keyboard import InlineKeyboardBuilder



router = Router()


cod_emoji = {
    "Thunderstorm": "Гроза⛈️",
    "Drizzle": "Дощик🌦️",
    "Rain": "Дощ🌧️",
    "Snow": "Сніг🌨️",
    "Clear": "Сонячна☀️",
    "Clouds": "Хмарно☁️",
    "Fog": "Туман 🌫️",
}


best_of_luck = ["До побачення!", "Бажаю успіхів!", "Нехай щастить!",
                "Всього найкращого!", "До зустрічі!", "Успіхів та гарного дня!",
                "Бережіть себе!", "До скорої зустрічі!", "Хай удача супроводжує вас!",
                "Удачі!", "Бажаю вам вдалих справ!", "Всього найкращого вам!"]


@router.message(Command("start"))
async def ask_user(msg: Message):
    await msg.answer(f"Привіт веди місто щоб дізнатися погоду в ньому")


@router.message()
async def start_handler(message: types.Message):
    try:
        current_date = datetime.datetime.now()
        day_of_week = current_date.weekday()
        day_names = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        day_name = day_names[day_of_week]
        day_of_month = current_date.day
        month = current_date.month
        year = current_date.year

        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()

        city = data["name"]
        cur_waether = int(data["main"]["temp"])
        humidity = int(data["main"]["humidity"])
        pressure = int(data["main"]["pressure"])
        wind = int(data["wind"]["speed"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        weather = data["weather"][0]["main"]

        for key in cod_emoji:
            if key in weather:
                w = cod_emoji.get(key)
                break
            else:
                w = "Подивись в вікно (якщо воно ще є)"

        await message.reply(f"{day_name} <em>{day_of_month}-{month}-{year}</em>:\n"
                            f"  В місті:  {city}\n"
                            f"  Температура:  {cur_waether}°C\n"
                            f"  Вологість:    {humidity}%\n"
                            f"  Тиск:    {pressure}гПа\n"
                            f"  Швидкість вітру:  {wind}м/с\n"
                            f"  Захід сонця:  {sunset}\n"
                            f"  Погода:   {w}\n"
                            f"{random.choice(best_of_luck)}")
    except:
        await message.reply("Місто вказано не правильно")