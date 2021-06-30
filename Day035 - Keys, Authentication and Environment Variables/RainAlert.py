import requests

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
APIKEY = ""

MYLAT = 44.230480
MYLONG = -76.481247

parameters = {
    "lat":MYLAT,
    "lon":MYLONG,
    "exclude": "current,minutely,daily",
    "appid":APIKEY,
}

response = requests.get(ENDPOINT,params=parameters)
response.raise_for_status()

data = response.json()

twelveHourSlice = data["hourly"][0:12]

willRain = False
for hour in twelveHourSlice:
    if int(hour["weather"][0]["id"])<700:
        print("Bring an umbrella.")
        willRain = True
        break



