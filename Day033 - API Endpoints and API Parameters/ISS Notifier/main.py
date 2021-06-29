import requests
from datetime import datetime
import smtplib


MY_EMAIL = ""
MY_PASSWORD = ""
MY_LAT = 44.233753
MY_LONG = -76.4964

def issOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if ((MY_LAT-5) <= iss_latitude <= (MY_LAT+5)) and ((MY_LONG-5) <= iss_latitude <= (MY_LONG+5)):
        return True
    return False


def isNightTime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


if issOverhead() and isNightTime():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=MY_EMAIL, 
        msg="The ISS is above you in the sky"
    )





