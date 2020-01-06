"""
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu urllib.request, json oraz API MetaWeather.
"""

import json
import urllib.request
from urllib.request import Request

lokalizacja = input("Wpisz lokalizację dla której chciałbyś poznać pogode: ")
url = f'https://www.metaweather.com/api/location/search/?query={lokalizacja}'

zapytanie = Request(url)

with urllib.request.urlopen(zapytanie) as req:
    print(req.geturl())
    print(req.info())
    print(req.getcode())

    zawartosc = json.loads(req.read())
    city_id = zawartosc[0]['woeid']
    url2 = f'https://www.metaweather.com/api/location/{city_id}'

    zapytanie2 = Request(url2)

    with urllib.request.urlopen(zapytanie2) as req2:
        print(req2.geturl())
        print(req2.info())
        print(req2.getcode())

        zawartosc2 = json.loads(req2.read())
        print (f'Temperatura w miejscie o nazwie {zawartosc[0]["title"]} wynosi {zawartosc2["consolidated_weather"][0]["the_temp"]}')
