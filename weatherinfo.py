import requests
import os
from datetime import datetime

API_Key = 'e10265b54a4d18da4bae74c480daeafa'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

print(weather_data)


