import requests
from config import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5"

def get_weather(city):
    """Fetch current weather data for a city."""
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(f"{BASE_URL}/weather", params=params)
        response.raise_for_status()
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def get_forecast(city):
    """Fetch 5-day weather forecast for a city."""
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(f"{BASE_URL}/forecast", params=params)
        response.raise_for_status()
        data = response.json()
        
        forecast = []
        for entry in data['list']:
            forecast.append({
                'datetime': entry['dt_txt'],
                'temperature': entry['main']['temp'],
                'description': entry['weather'][0]['description'],
                'icon': entry['weather'][0]['icon']
            })
        return forecast
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}