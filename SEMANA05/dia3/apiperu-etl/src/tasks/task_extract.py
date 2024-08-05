import requests
from prefect import task
from config import Config
import csv

config = Config()

@task(name='extraer info de csv')
def task_extract_csv(file_csv):
    with open(file_csv,mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lista_csv = []
        for row in csv_reader:
            tupla_csv = (row['ruc'],row['venta'])
            lista_csv.append(tupla_csv)

    return lista_csv

@task(name="Extraer info de ruc")
def task_extract_ruc(lista_ruc):
    lista_ruc_completa = []
    for tupla_ruc in lista_ruc:
        ruc = tupla_ruc[0]
        venta = tupla_ruc[1]

        print("RUC :",ruc)

        data_request = {
            "ruc": ruc 
        }

        headers_request = {
            "Authorization": "Bearer " + config.api_token,
            "Content-Type": "application/json"
        }
        response = requests.post(config.api_url_ruc,
                                json=data_request,
                                headers=headers_request)
        
        if response.status_code == 200:
            response_ruc = response.json()
            if response_ruc['success'] == True:
                #print(data_alumnos)
                data_ruc = response_ruc['data']
                tupla_ruc_completo = (data_ruc['ruc'],
                                    data_ruc['nombre_o_razon_social'],
                                    data_ruc['departamento'],
                                    data_ruc['direccion'],
                                    venta)
                lista_ruc_completa.append(tupla_ruc_completo)
            else:
                print("ERROR AL CONECTARSE AL API : ",response_ruc['message'])
        else:
            print(f"error : {response.status_code}")

    return lista_ruc_completa