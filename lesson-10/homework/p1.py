import requests
import random


API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
city = 'Tashkent'
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(weather_url)
weather_data = response.json()

if weather_data['cod'] == 200:
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    print(f"Weather in {city}: {description}, Temperature: {temp}°C, Humidity: {humidity}%")
else:
    print("Failed to retrieve weather data.")