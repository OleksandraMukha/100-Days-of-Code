import requests
from datetime import datetime
import os 
import base64


APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
WEIGHT = "54"
HEIGHT = "164"
AGE = "21"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/3effb38a49469d80cb0265adba12e27a/myWorkouts/workouts"
encoded_auth_header = "c2FzaGFtdWtoYTpZKyhXVG0zVTJhKzNWTm1L"


exercise_text = input("Tell me which exercises you did: ")
#Authentification
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    headers_sheety = {
    "Authorization": f"Basic {encoded_auth_header}"
}
    
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=headers_sheety)
    print(sheet_response.text)