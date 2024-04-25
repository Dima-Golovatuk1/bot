import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_waether = int(data["main"]["temp"])



        print(f"в місті: {city}\n"
              f"Температура⛈️: {cur_waether}°C")
    except Exception as ex:
        print(ex)
        print("Місто названо не правильно")


def main():
    city = input(f"Ведіть назву міста")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()


