import requests
from dotenv import load_dotenv
import os
## Parse a .env file and then load all the variables found as environment variables.
load_dotenv()

api_key = os.getenv('API_KEY')

# fetches the latitude and longitude of a city using geocoder api
def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    
    data = resp[0]
    lat, long = data.get('lat'), data.get('lon')
    return lat, long

# fetches the current weather using the openweathermap api
def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = {
        'main': resp.get('weather')[0].get('main'),
        'description': resp.get('weather')[0].get('description'),
        'icon': resp.get('weather')[0].get('icon'),
        'temp': int(resp.get('main').get('temp'))
    }
    
    return data

def get_weather(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    
    return weather_data

if __name__ == '__main__':
    lat, lon = get_lat_lon('Khansahib', 'Khansahib', 'India', api_key)
    weather_data = get_current_weather(lat, lon, api_key)
