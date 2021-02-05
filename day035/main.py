import os
import requests
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
api_key = os.environ['OWM_API_KEY']
twilio_did = os.environ['TWILIO_DID']
cell_number = os.environ['CELL_NUMBER']

location = {
    "city": "minneapolis",
    "lat": 44.977753,
    "lng": -93.265015
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params={"units": "imperial", "exclude": "current,daily", "lat": location["lat"], "lon": location["lng"], "appid": api_key}
)
response.raise_for_status()
data = response.json()
hours = data["hourly"]
next12_hours = hours[:12]

weather = []
for hour in next12_hours:
    weather.append(hour['weather'][0]['description'])

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="\n".join(weather),
    from_=twilio_did,
    to=cell_number
)

print(message.status)