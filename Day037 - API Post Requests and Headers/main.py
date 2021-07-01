import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixelaEndpoint = "https://pixe.la/v1/users"
userParams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixelaEndpoint, json=userParams)
# print(response.text)

graphEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN":TOKEN,
}
graphConfig = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji",
}

# response = requests.post(url=graphEndpoint, json=graphConfig, headers=header)
# print(response.text)

pixelCreationEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{graphConfig['id']}"
pixelData = {
    "date":str(datetime.now().strftime("%Y%m%d")),
    "quantity": "25.47",
}

# response = requests.post(url=pixelCreationEndpoint, json=pixelData, headers=header)
# print(response.text)


updateEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{graphConfig['id']}/{datetime.now().strftime('%Y%m%d')}"
updatePixelData = {
    "quantity": "50",
}

# response = requests.put(url=updateEndpoint, json=updatePixelData, headers=header)
# print(response.text)


deleteEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{graphConfig['id']}/{datetime.now().strftime('%Y%m%d')}"

# response = requests.delete(url=deleteEndpoint,headers=header)
# print(response.text)