# Запросы с параметрами
# От пользователя спросить название города
# Отправить запрос на сервис openweathermap
# Получить данные про погоду в этом городе

# ---------------------------------------------------
import requests
import json
from datetime import datetime

API_KEY = "ccdd17f96d6dd55e8a75e51f425e8112"
URL = "https://api.openweathermap.org/data/2.5/weather"
weather_json = []
time = datetime.now().strftime("%d_%m_%Y___%H_%M_%S")



while True:
    city_name = input("Название города: ")
    if city_name == "stop":
        break
    try:
        response = requests.get(url=URL,
                                params={
                                    "q": city_name,
                                    "appid": API_KEY,
                                    "units": "metric",
                                    "lang": "ru"
                                })

        weather_data = response.json()
        # print(weather_data)
        # Обработать эти данные
        # desc
        desc = weather_data['weather'][0]['description']
        # temp
        temp = weather_data['main']['temp']
        # feels_like
        feels_like = weather_data['main']['feels_like']
        # wind_speed
        wind_speed = weather_data['wind']['speed']
        timezone = weather_data['timezone']
        # sunrise
        sunrise = datetime.utcfromtimestamp(timezone + weather_data['sys']['sunrise'])
        # sunset
        sunset = datetime.utcfromtimestamp(timezone + weather_data['sys']['sunset'])
        # В красивом виде выдать пользователю


        weather_json.append({
            "Название города": city_name,
            "Описание погоды": desc,
            "Температура воздуха": temp,
            "Ощущается как": feels_like,
            "Скорость ветра": wind_speed,
            "Восход солнца": str(sunrise),
            "Закат солнца": str(sunset)
        })

        print(f"""Сейчас в городе {city_name}, {desc} погода.
Температура воздуха: {temp} градусов °С,
Но ощущается как: {feels_like} градусов °С.
Скорость ветра: {wind_speed} м/сек.
Восход солнца: {sunrise},
Закат солнца: {sunset} !""")
    except:
        print("Неправильное название города !")


with open(f"weather_{time}.json", mode="a", encoding="UTF-8") as file:
    json.dump(weather_json, file, ensure_ascii=False, indent=4)

