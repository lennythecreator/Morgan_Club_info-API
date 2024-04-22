import requests


BASE ="http://127.0.0.1:5000/"

response = requests.put(BASE + "students/Lenny/23/Junior/Playing",headers={'Content-Type': 'application/json'})
print(response.json())