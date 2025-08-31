import requests
from config import API_KEY

BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"
city = input("Enter the city name: ")

params = {"q": city, "appid": API_KEY, "units": "metric"}

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    main = data["main"]
    weather = data["weather"][0]
    print(
        f"Weather in {city}: {weather['description']},\n"
        f"Temperature: {main['temp']}°C,\n"
        f"Humidity: {main['humidity']}%"
    )
except requests.exceptions.HTTPError:
    print("City not found or API error occurred.")
except Exception as e:
    print("Error:", e)
