import requests
from datetime import datetime

# Configure for your stats
GENDER = "male"
WEIGHT_KG = "175"
HEIGHT_CM = "175"
AGE = "21"

# Enter your  Nutritionix AppID and API Key
APP_ID = ""
API_KEY = ""

# Fill out with your Nutritionix endpoint as well as sheety Endpoint for 
exerciseEndpoint = ""
sheetEndpoint = ""

# Ask user for information on their workout
exerciseText = input("Tell me which exercises you did: ")


# creation of header for API Post for the Nutritionix API
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exerciseText,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Perform the post request to Nutritionix API and receive the result
response = requests.post(exerciseEndpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


# For all of the exercises received back from the Nutritionix API add a line to the Google sheet using the sheety endpoint and a post request
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.post(url=sheetEndpoint, json=sheet_inputs)