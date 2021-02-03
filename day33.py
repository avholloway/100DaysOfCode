import time
import requests
from datetime import datetime as dt

my_location = {
    "latitude": 45.098120,
    "longitude": -93.444530
}

parameters = {
    "lat": my_location["latitude"],
    "lng": my_location["longitude"],
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

def is_dark_now(sunrise, sunset):
    now = int(str(dt.utcnow()).split(" ")[1].split(":")[0])
    return now < sunrise or now > sunset

def is_iss_overhead(iss, you):
    margin = 5
    lat_distance = abs(you["latitude"] - iss["latitude"])
    lng_distance = abs(you["longitude"] - iss["longitude"])
    return lat_distance <= margin and lng_distance <= margin

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_position = {k:float(v) for k, v in data["iss_position"].items()}

while True:
    if is_dark_now(sunrise, sunset) and is_iss_overhead(iss_position, my_location):
        print("Hey! The ISS is over your house! Go outside and look for it!")
    else:
        print("Nothing to see here. Move it along.")
    time.sleep(60)