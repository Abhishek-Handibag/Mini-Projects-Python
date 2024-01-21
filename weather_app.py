import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        display_weather(weather_data)
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")


def display_weather(weather_data):
    city = weather_data['name']
    country = weather_data['sys']['country']
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

    print(f"Weather in {city}, {country}:")
    print(f"Description: {description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")


if __name__ == "__main__":
    api_key = "c0a2ad1a9d3dac048da25758bb4b382d"

    city = input("Enter city name: ")
    get_weather(api_key, city)
