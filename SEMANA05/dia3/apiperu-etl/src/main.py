from prefect import flow
from tasks.task_extract import(
    task_extract_ruc,
    task_extract_csv
)
from tasks.task_load import (
    task_load_ruc
)

PATH_CSV = './resources/ruc.csv'


@flow(name='ETL APIPERU')
def main_flow():
    lista_ruc = task_extract_csv(PATH_CSV)
    print(lista_ruc)
    lista_ruc_completa = task_extract_ruc(lista_ruc)
    print(lista_ruc_completa)
    task_load_ruc(lista_ruc_completa)

if __name__ == '__main__':
    main_flow()