import requests
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = "461d4f5dfce831e8d53650d808c22e77"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=461d4f5dfce831e8d53650d808c22e77&units=metric"

response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    print("City not found.")
else:
    main = data["main"]
    weather = data["weather"][0]["description"]
    wind = data["wind"]["speed"]
    clouds = data["clouds"]["all"]
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")

    print(f"\nWeather in {city.capitalize()}:\n")
    print(f"Temperature: {main['temp']}°C")
    print(f"Feels like: {main['feels_like']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Wind Speed: {wind} m/s")
    print(f"Cloudiness: {clouds}%")
    print(f"Condition: {weather.capitalize()}")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

    # Visualization
    labels = ['Temp (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Wind (m/s)', 'Cloudiness (%)']
    values = [main['temp'], main['feels_like'], main['humidity'], wind, clouds]
    colors = ['skyblue', 'orange', 'lightgreen', 'lightcoral', 'gray']

    plt.barh(labels, values, color=colors)
    plt.title(f"Weather Stats for {city.capitalize()} - {weather.capitalize()}")
    plt.xlabel("Values")
    plt.tight_layout()
    plt.show()



