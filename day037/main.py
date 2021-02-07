import os
import requests
from datetime import datetime as dt, timedelta

# === Setup ===================================================================

pixela = "https://pixe.la"
version = "v1"

username = os.environ["username"]
token = os.environ["token"]

graph_id = "flossing101"
graph_name = "Flossing"

today = dt.now().strftime("%Y%m%d")

# === Create User =============================================================

endpoint = f"{pixela}/{version}/users"
data = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Already created the user at https://pixe.la/@anthony
# response = requests.post(url=endpoint, json=data)
# response.raise_for_status()
# print(response.text)

# === Create Graph ============================================================

endpoint = f"{pixela}/{version}/users/{username}/graphs"
headers = {
    "X-USER-TOKEN": token
}
data = {
    "id": graph_id,
    "name": graph_name,
    "unit": "commit",
    "type": "int",
    "color": "sora",
    "timezone": "America/Chicago"
}

# Graph already created
# response = requests.post(url=endpoint, headers=headers, json=data)
# response.raise_for_status()
# print(response.text)

# === Add Data to the Graph ===================================================

endpoint = f"{pixela}/{version}/users/{username}/graphs/{graph_id}"
headers = {
    "X-USER-TOKEN": token
}

# Back dating some work for the past 36 days
# for i in range (36, 0, -1):
#     day = (dt.now() - timedelta(i)).strftime("%Y%m%d")
#     print(f"Setting commit for {day}...", end="")
#     data = {
#         "date": day,
#         "quantity": "1"
#     }
#     response = requests.post(url=endpoint, headers=headers, json=data)
#     print(response.status_code)

# === Update Data on the Graph ================================================

# This will also add data to the graph for the given day and quantity

day = dt(year=2021, month=1, day=13).strftime("%Y%m%d")
endpoint = f"{pixela}/{version}/users/{username}/graphs/{graph_id}/{day}"
headers = {
    "X-USER-TOKEN": token
}
data = {
    "quantity": "1"
}

response = requests.put(url=endpoint, headers=headers, json=data)
response.raise_for_status()
print(response.text)

# === Delete Data on the Graph ================================================

day = dt(year=2021, month=1, day=13).strftime("%Y%m%d")
endpoint = f"{pixela}/{version}/users/{username}/graphs/{graph_id}/{day}"
headers = {
    "X-USER-TOKEN": token
}

# response = requests.delete(url=endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)