import requests
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

API_KEY = "c83481b4a6c6d5ab83aa5f1559d69b88"

location = {
    "city": "minneapolis",
    "lat": 44.977753,
    "lng": -93.265015
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params={"units": "imperial", "exclude": "current,daily", "lat": location["lat"], "lon": location["lng"], "appid": API_KEY}
)
response.raise_for_status()
data = response.json()
hours = data["hourly"]
next12_hours = hours[:12]

for hour in next12_hours:
    weather = hour['weather'][0]
    print(f"Weather: {weather['id']} ({weather['description']})")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_='+16124293700',
    to='+16128892514'
)

print(message.status)