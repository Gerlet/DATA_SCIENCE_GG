from prefect import flow
from tasks.task_extract import(
    task_extract_dni,
    task_extract_csv
)
from tasks.task_load import (
    task_load_alumnos
)

PATH_CSV = './resources/alumnos.csv'


@flow(name='ETL APIPERU')
def main_flow():
    lista_alumnos = task_extract_csv(PATH_CSV)
    print(lista_alumnos)
    lista_alumnos_completa = task_extract_dni(lista_alumnos)
    print(lista_alumnos_completa)
    task_load_alumnos(lista_alumnos_completa)

if __name__ == '__main__':
    main_flow()