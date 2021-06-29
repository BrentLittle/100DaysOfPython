import requests
from datetime import datetime





### Location of ISS 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

position = data["iss_position"]
print(f"Position: {position}")

long = data["iss_position"]["longitude"]
print(f"Longitude: {long}")

lat = data["iss_position"]["latitude"]
print(f"Latitude: {lat}")

position = (long,lat)
print(position)





### Sunrise sunset times

MY_LAT = 44.233753
MY_LONG = -76.4964

params = {
    "lat" :MY_LAT,
    "lng" :MY_LONG,
    "formatted": 0,
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params = params)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = data["results"]["sunrise"].split("T")
sunriseHour = sunrise[1].split(":")[0]
print(sunrise)
print(sunriseHour)

sunset = data["results"]["sunset"].split("T")
sunsetHour = sunset[1].split(":")[0]
print(sunset)
print(sunsetHour)