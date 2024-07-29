import requests
import os
from decouple import config

token = config('API_TOKEN')
url_dni = 'https://apiperu.dev/api/dni'

dni = input("ingrese dni :")

data_request = {
    "dni": dni 
}

headers_request = {
    "Authorization": "Bearer " + str(token),
    "Content-Type": "application/json"
}

response = requests.post(url_dni,json=data_request,headers=headers_request)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}")