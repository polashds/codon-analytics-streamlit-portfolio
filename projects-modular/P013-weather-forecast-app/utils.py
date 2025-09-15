
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get('main'):
        return {
            'City': city,
            'Temperature (°C)': res['main']['temp'],
            'Humidity (%)': res['main']['humidity'],
            'Weather': res['weather'][0]['description']
        }
    return None