import os
import requests
import datetime as dt

API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2"
NUTRITIONIX_POST_EXERCISE_ENDPOINT = "/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/97fc889332836425c14090a0171f2b63/workoutTracking/workouts"
SHEETY_BEARER_TOKEN = os.environ["SHEETY_TOKEN"]
today = dt.datetime.today()
formatted_today = today.strftime("%d/%m/%Y")
formatted_hour = today.strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutritionix_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 108,
    "height_cm": 185,
    "age": 22
}

nutritionix_post_response = requests.post(url=f"{NUTRITIONIX_ENDPOINT}{NUTRITIONIX_POST_EXERCISE_ENDPOINT}",
                                          json=nutritionix_body, headers=headers)
nutritionix_post_response.raise_for_status()
nutritionix_result = nutritionix_post_response.json()

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for workout in nutritionix_result["exercises"]:
    sheety_body = {
        "workout": {
            "date": formatted_today,
            "time": formatted_hour,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }
    sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_headers)
    sheety_post_response.raise_for_status()
