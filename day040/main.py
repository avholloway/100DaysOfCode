import sys
from data_manager import DataManager
# from flight_search import FlightSearch
# from flight_data import FlightData
# from notification_manager import NotificationManager

dm = DataManager()

first_name = input("Firstname: ")
last_name = input("Lastname: ")
email = input("Email: ")
confirm_email = input("Confirm Email: ")
if email != confirm_email:
    print("Wooow....")
    sys.exit(1)
dm.add_user(first_name, last_name, email)
print("You're in the club!")

# fs = FlightSearch()
# nm = NotificationManager()

# for trip in dm.trips:
#     found = fs.upcoming("MSP", trip["iataCode"], trip["lowestPrice"])
#     if found["price"] < trip["lowestPrice"]:
#         nm.send(f"Found a cheap ${found['price']} flight from MSP to {trip['iataCode']}!")