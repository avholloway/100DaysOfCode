import os
import requests

class DataManager:
    def __init__(self):
        self.SHEETY_API_HOST = "https://api.sheety.co"
        self.SHEETY_API_KEY = os.getenv('SHEETY_API_KEY')
        self.SHEETY_UID = os.getenv('SHEETY_UID')
        self.SHEETY_PROJECT = "day40FlightDeals"
        self.SHEETY_PRICES_SHEET = "prices"
        self.SHEETY_USERS_SHEET = "users"
        self.SHEETY_HEADERS = {
            "Authorization": f"Bearer {self.SHEETY_API_KEY}"
        }
        self.trips = self.get_trips()

    def get_trips(self):
        ENDPOINT = f"{self.SHEETY_API_HOST}/{self.SHEETY_UID}/{self.SHEETY_PROJECT}/{self.SHEETY_PRICES_SHEET}"
        response = requests.get(ENDPOINT, headers=self.SHEETY_HEADERS)
        response.raise_for_status()
        return response.json()["prices"]

    def add_user(self, f, l, e):
        DATA = {
            "user": {
                "firstName": f,
                "lastName": l,
                "email": e
            }
        }
        ENDPOINT = f"{self.SHEETY_API_HOST}/{self.SHEETY_UID}/{self.SHEETY_PROJECT}/{self.SHEETY_USERS_SHEET}"
        response = requests.post(ENDPOINT, headers=self.SHEETY_HEADERS, json=DATA)
        response.raise_for_status()