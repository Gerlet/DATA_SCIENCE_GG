import requests
from prefect import task
from config import Config
import csv

config = Config()

@task(name='extraer info de csv')
def task_extract_csv(file_csv):
    with open(file_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lista_csv = []
        for row in csv_reader:
            tupla_csv = (row['ruc'], row['venta_anual'])
            lista_csv.append(tupla_csv)
    return lista_csv

@task(name="Extraer info de ruc")
def task_extract_ruc(lista_ruc):
    lista_ruc_completa = []
    for tupla_ruc in lista_ruc:
        ruc = tupla_ruc[0]
        venta_anual = tupla_ruc[1]

        print("RUC:", ruc)

        headers_request = {
            "Authorization": "Bearer " + config.api_token,
            "Content-Type": "application/json"
        }

        response = requests.get(config.api_url_ruc + ruc, headers=headers_request)
        
        if response.status_code == 200:
            print("200 ok")
            response_ruc = response.json()

            if 'success' in response_ruc:
                if response_ruc['success']:
                    data_ruc = response_ruc['data']
                    tupla_ruc_completo = (
                        data_ruc['numeroDocumento'],
                        data_ruc['razonSocial'],
                        data_ruc['direccion'],
                        data_ruc['tipo']
                    )
                    lista_ruc_completa.append(tupla_ruc_completo)
                else:
                    print("ERROR AL CONECTARSE AL API:", response_ruc['message'])
            else:
                print(f"Respuesta inesperada de la API para el RUC {ruc}: {response_ruc}")
        else:
            print(f"Error: {response.status_code}")

    return lista_ruc_completa
