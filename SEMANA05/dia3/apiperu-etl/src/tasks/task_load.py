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
def task_load_ruc(ruc):
    try:
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_empresa"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_empresa(
        id INT AUTO_INCREMENT PRIMARY KEY,
        numeroDocumento VARCHAR(20),
        razonSocial VARCHAR(255),
        direccion VARCHAR(255),
        tipo VARCHAR(100),
        fecha_creacion DATETIME default CURRENT_TIMESTAMP)
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_empresa(numeroDocumento,razonSocial,direccion,tipo)
        values(%s,%s,%s,%s)
        """

        for rut in ruc:
            cursor.execute(query_insert,rut)

        conn.commit()
        cursor.close()
        conn.close()
        print('datos guardados en bd...')

    except mysql.connector.Error as err:
        print(err)