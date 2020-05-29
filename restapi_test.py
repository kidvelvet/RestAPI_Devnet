#! /usr/bin/env python

import os # attempt to read API key from the environment variable (OW_API_KEY)
import sys # access an optional argument to write raw JSON output to a file
import requests
import json
from getpass import getpass

# insert your api key here for the location
print()
city_name = input('Enter your the City of where you want know the current weather: ')


# insert your api key here for the location
print()
state = input('Enter your the State whole name of where you want know the current weather: ')

# who do you want to send this information to?
# print('To whom would you like to send this weather information to? Enter their email now.')
# whoto = input()

weather_api_key = os.getenv('OW_API_KEY') # check for the existance of the environment variable (OW_API_KEY)
if not weather_api_key: # if the environment variable (OW_API_KEY) returns None, prompt for an API key
    weather_api_key = getpass('Enter your weather AKI key: ')

# webexapikey = getpass('enter your webex api key now.')

wurl = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state}&units=imperial&appid={weather_api_key}'

headers= {
    'Accept': 'application/json' # the API doc says it supports JSON, XML, and HTML so it's good to specify the one you want
}

response = requests.request("GET", wurl, headers=headers)

# Check for the presence of the argument 'debug' and, if present, write the raw data to a file
# Usage: python rest_test.py debug
if len(sys.argv) > 1:
    if sys.argv[1] == 'debug':
        import json
        with open(f'{sys.argv[0]}_response.json', 'w') as file:
            file.write(json.dumps(response.json(), indent=2))

message = response.json()
print()
print(message['name'])
print(message['main']['temp'])
for weather in message['weather']:
    print(weather['main'])
print()
