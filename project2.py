import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()

        temperature_kelvin = data['main']['temp']

        temperature_celsius = temperature_kelvin - 273.15
        print(f"Current temperature in {city_name}: {temperature_celsius:.2f}°C")
    else:
        print("Invalid data or error in fetching data")

if __name__ == "__main__":
    api_key = "dda42cd162540a6c86e786168fd8b57b"  

    city_name = input("Enter the city name: ")

    get_weather(city_name, api_key)