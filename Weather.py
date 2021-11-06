import requests
import json
weatherAPIKey = '5bc0f788b7783ecdb4cad9b0cc0c69b8'
city = 'Amherst'
weatherUrl = f'http://api.openweathermap.org/data/2.5/weather?q=Amherst&appid={weatherAPIKey}'

def getCurrentWeather():
    weatherResponse = requests.get(weatherUrl)
    return weatherResponse.json()