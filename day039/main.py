from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

for trip in dm.trips:
    found = fs.upcoming("MSP", trip["iataCode"], trip["lowestPrice"])
    if found["price"] < trip["lowestPrice"]:
        nm.send(f"Found a cheap ${found['price']} flight from MSP to {trip['iataCode']}!")