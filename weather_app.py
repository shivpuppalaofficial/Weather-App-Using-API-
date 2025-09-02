
import requests


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        print("❌ Failed to fetch weather data")
        return None


def main():
    api_key = "YOUR_API_KEY"  # 🔑 Replace with your free OpenWeather API key
    city = input("Enter city name: ")

    weather = get_weather(city, api_key)
    if weather:
        print(f"✅ Weather in {weather['city']}:")
        print(f"🌡 {weather['temperature']}°C, {weather['description'].capitalize()}")


if __name__ == "__main__":
    main()
