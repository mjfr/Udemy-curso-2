import requests
import os

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/97fc889332836425c14090a0171f2b63/flightDeals/users"
SHEETY_HEADERS = {
    "Authorization": f"Bearer {os.environ['SHEETY_BEARER']}"
}

first_name = input("Welcome to Matheus's Flight Club.\nWe find the best flight deals and email you.\nWhat is your"
                   " first name?\n").title()
last_name = input("What is your last name?\n").title()
email = input("What is your email?\n").lower()
while email != input("Type your email again.\n").lower():
    print("The email confirmation does not match the first email field.")

sheety_body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

sheety_post_user_response = requests.post(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_HEADERS, json=sheety_body)
sheety_post_user_response.raise_for_status()
print(sheety_post_user_response.text)
