import os
import requests
from datetime import datetime as dt, timedelta as td

class FlightSearch:
    def __init__(self):
        self.host = "https://tequila-api.kiwi.com"
        self.version = "v2"
        self.KIWI_API_KEY = os.getenv('KIWI_API_KEY')
        
    def upcoming(self, from_, to, price):
        endpoint = f"{self.host}/{self.version}/search"
        tomorrow = (dt.now() + td(1)).strftime("%d/%m/%Y")
        six_months = (dt.now() + td(180)).strftime("%d/%m/%Y")
        headers = {
            "Accept-Encoding": "gzip",
            "Accept": "application/json"
        }
        parameters = {
            "apikey": self.KIWI_API_KEY,
            "fly_from": from_,
            "fly_to": to,
            "dateFrom": tomorrow,
            "dateTo": six_months,
            "curr": "USD",
            "price_from": 1,
            "price_to": price
        }
        response = requests.get(endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()["data"]
        try:
            cheapest = min(data, key=lambda flight: flight["price"])
        except ValueError:
            cheapest = {"price": float('inf')}
        return cheapest
