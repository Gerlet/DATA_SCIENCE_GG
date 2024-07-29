import mysql.connector
from config import Config
from prefect import task

config = Config()

conn = mysql.connector.connect(
            user=config.mysql_user,
            password=config.mysql_password,
            host=config.mysql_host,
            database=config.mysql_database
        )


@task(name='carga de info en bd')
def task_load_alumnos(alumnos):
    try:
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_postulante"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_postulante(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dni VARCHAR(20),
        nombres VARCHAR(255),
        apellidos VARCHAR(255),
        celular VARCHAR(20),
        fecha_creacion DATETIME default CURRENT_TIMESTAMP)
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_postulante(dni,nombres,apellidos,celular)
        values(%s,%s,%s,%s)
        """

        for alumno in alumnos:
            cursor.execute(query_insert,alumno)

        conn.commit()
        cursor.close()
        conn.close()
        print('datos guardados en bd...')

    except mysql.connector.Error as err:
        print(err)