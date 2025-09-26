import requests

s = "Москва"
try:
    res = requests.get("https://raw.githubusercontent.com/pensnarik/russian-cities/master/russian-cities.json").json
    cities = [city['name'] for city in res]
    
    if s in cities:
        weather = requests.get(f"http://wttr.in/{s}?format=3").text
        print(weather)

except Exception as e:
    print(e)