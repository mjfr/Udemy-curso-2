import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Caso não retorne o código 200, podemos levantar uma exception
# error_response = requests.get(url="http://api.open-notify.org/iss-now.jso")
# error_response.raise_for_status()

data = response.json()  # Retorna o json dentro de um dictionary
print(data)
print(data["iss_position"])
print(data["iss_position"]["longitude"])

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

