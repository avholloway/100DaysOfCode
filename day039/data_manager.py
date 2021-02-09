import os
import requests

class DataManager:
    def __init__(self):
        self.SHEETY_API_HOST = "https://api.sheety.co"
        self.SHEETY_API_KEY = os.getenv('SHEETY_API_KEY')
        self.SHEETY_UID = os.getenv('SHEETY_UID')
        self.SHEETY_PROJECT = "day39FlightDeals"
        self.SHEETY_SHEET = "prices"
        self.SHEETY_ENDPOINT = f"{self.SHEETY_API_HOST}/{self.SHEETY_UID}/{self.SHEETY_PROJECT}/{self.SHEETY_SHEET}"
        self.SHEETY_HEADERS = {
            "Authorization": f"Bearer {self.SHEETY_API_KEY}"
        }
        self.trips = self.get_trips()

    def get_trips(self):
        response = requests.get(self.SHEETY_ENDPOINT, headers=self.SHEETY_HEADERS)
        response.raise_for_status()
        return response.json()["prices"]