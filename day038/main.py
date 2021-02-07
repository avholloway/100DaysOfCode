import os
import sys
import json
import requests
from datetime import datetime as dt

# === User Interaction ========================================================

activity = input("Input: ")

# === NutritionIX API Info ====================================================

NUTRX_API_HOST = "https://trackapi.nutritionix.com"
NUTRX_API_VERSION = "v2"
NUTRX_APP_ID = os.getenv('NUTRX_APP_ID')
NUTRX_APP_KEY = os.getenv('NUTRX_APP_KEY')
NUTRX_HEADERS = {
    "x-app-id": NUTRX_APP_ID,
    "x-app-key": NUTRX_APP_KEY,
    "x-remote-user-id":  "avholloway"
}
NUTRX_ENDPOINT = f"{NUTRX_API_HOST}/{NUTRX_API_VERSION}/natural/exercise"
NUTRX_DATA = {
    "query": activity,
    "gender": "male",
    "weight_kg": 102,
    "height_cm": 188,
    "age": 38
}

response = requests.post(url=NUTRX_ENDPOINT, headers=NUTRX_HEADERS, json=NUTRX_DATA)
response.raise_for_status()
data = response.json()

exercise = data["exercises"][0]
name = exercise["name"].title()
duration = int(exercise["duration_min"])
calories = int(exercise["nf_calories"])

# === Sheetly API Info ========================================================

SHEETLY_API_HOST = "https://api.sheety.co"
SHEETLY_UID = os.getenv('SHEETLY_UID')
SHEETLY_API_KEY = os.getenv('SHEETLY_API_KEY')
SHEETLY_PROJECT = "day38MyWorkouts"
SHEETLY_ENDPOINT = f"{SHEETLY_API_HOST}/{SHEETLY_UID}/{SHEETLY_PROJECT}/workouts"
SHEETLY_HEADERS = {
    "Authorization": f"Bearer {SHEETLY_API_KEY}"
}
activity_date = dt.now().strftime("%d/%m/%Y")
activity_time = dt.now().strftime("%H:%M:%S")
SHEETLY_DATA = {
    "workout": {
        "date": activity_date,
        "time": activity_time,
        "exercise": name,
        "duration": duration,
        "calories": calories
    }
}
response = requests.post(url=SHEETLY_ENDPOINT, headers=SHEETLY_HEADERS, json=SHEETLY_DATA)
response.raise_for_status()

if response.status_code == 200:
    print(f"I have logged your {name} for today! You burned {calories} calories! Nice!")