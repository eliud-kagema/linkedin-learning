import requests
import json
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '2b8c62f426a0ca8ffeb5c9e8d068c6f3', 'q': 'Nairobi,Kenya' }

response = requests.get(baseUrl, params=parameters)

print(response.content)