#! python3
"""
quickWeather.py - Prints the weather for a location from the command line
"""

import json
import requests
import sys

API_KEY = '6c11597eb84c82ced354a5db5e302ef7'
# Compute location from the command line
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={cityName}&cnt=3&APPID={key}'.format(cityName=location,
                                                                                                    key=API_KEY)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions
w = weatherData['list']
print('Current weather in {}:'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
