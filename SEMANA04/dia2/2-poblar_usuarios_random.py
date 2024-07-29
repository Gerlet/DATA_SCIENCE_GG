import requests
import mysql.connector

def get_random_users(count=100):
    url = f'https://randomuser.me/api/?results={count}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print('error :',response.status_code)
        return []
    
def insert_users_to_mysql(users):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_codigo'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS tbl_usuario(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       nombre VARCHAR(255),
                       email VARCHAR(255),
                       pais VARCHAR(255),
                       foto VARCHAR(255)
                       )
                       """)
        
        for usuario in users:
             nombre = usuario['name']['first'] + ' ' + usuario['name']['last']
             pais = usuario['location']['country']
             email = usuario['email']
             foto = usuario['picture']['large']

             cursor.execute("""
                            INSERT INTO tbl_usuario(nombre,email,pais,foto)
                            values(%s,%s,%s,%s)
                            """,(nombre,email,pais,foto))
             
             connection.commit()
        print('usuarios insertados exitosamente')

count_usuarios = int(input("inserte cantidad de usuarios a extraer : "))
usuarios = get_random_users(count_usuarios)
#print(usuarios)
insert_users_to_mysql(usuarios)