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
            tupla_csv = (row['dni'],row['celular'])
            lista_csv.append(tupla_csv)

    return lista_csv

@task(name="Extraer info de dni")
def task_extract_dni(lista_alumnos):
    lista_alumnos_completa = []
    for tupla_alumno in lista_alumnos:
        dni = tupla_alumno[0]
        celular = tupla_alumno[1]

        print("DNI :",dni)

        data_request = {
            "dni": dni 
        }

        headers_request = {
            "Authorization": "Bearer " + config.api_token,
            "Content-Type": "application/json"
        }
        response = requests.post(config.api_url_dni,
                                json=data_request,
                                headers=headers_request)
        
        if response.status_code == 200:
            response_alumnos = response.json()
            if response_alumnos['success'] == True:
                #print(data_alumnos)
                data_alumnos = response_alumnos['data']
                tupla_alumno_completo = (data_alumnos['numero'],
                                    data_alumnos['nombres'],
                                    data_alumnos['apellido_paterno'] + ' ' + data_alumnos['apellido_materno'],
                                    celular)
                lista_alumnos_completa.append(tupla_alumno_completo)
            else:
                print("ERROR AL CONECTARSE AL API : ",response_alumnos['message'])
        else:
            print(f"error : {response.status_code}")

    return lista_alumnos_completa