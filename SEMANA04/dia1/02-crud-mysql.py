import os
import tabulate
import time
import mysql.connector

lista_alumnos = []
ANCHO = 50
opcion = 0



def mostrar_menu(ancho):
    print("="*ancho)
    print(" " * 10 + "CRUD DE ALUMNOS")
    print("="*ancho)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("="*ancho)


############### BASE DE DATOS ############
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_codigo'
    )

def consultar_alumnos():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    query = "select id,nombre,email,celular from tbl_alumno"
    cursor.execute(query)
    alumnos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return alumnos

def insertar_alumno(nombre,email,celular):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "insert into tbl_alumno(nombre,email,celular) values (%s,%s,%s)"
    cursor.execute(query,(nombre,email,celular))
    conexion.commit()
    cursor.close()
    conexion.close()


def buscar_alumno(valor_busqueda):
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    query = "select * from tbl_alumno where email = %s"
    cursor.execute(query,(valor_busqueda,))
    alumno = cursor.fetchone()
    cursor.close()
    conexion.close()
    return alumno

def actualizar_alumno(id,nombre,email,celular):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "UPDATE tbl_alumno SET nombre = %s,email = %s, celular = %s where id=%s"
    cursor.execute(query,(nombre,email,celular,id))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_alumno(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = 'DELETE FROM tbl_alumno WHERE id = %s'
    cursor.execute(query,(id,))
    conexion.commit()
    cursor.close()
    conexion.close()

while(opcion < 5):
    os.system("clear")
    mostrar_menu(ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR ALUMNO")
        print("="*ANCHO)
        nombre = input("NOMBRE : ")
        email = input("EMAIL : ")
        celular = input("CELULAR : ")
        insertar_alumno(nombre,email,celular)
        print(" ALUMNO REGISTRADO CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR ALUMNOS")
        print("="*ANCHO)
        cabeceras = ["ID","NOMBRE","EMAIL","CELULAR"]
        lista_alumnos = consultar_alumnos()
        tabla = [alumno.values() for alumno in lista_alumnos]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE EMAIL DEL ALUMNO A ACTUALIZAR :')
        alumno = buscar_alumno(valor_busqueda)
        if not alumno:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            print(f" ALUMNO A ACTUALIZAR : {alumno['nombre']}")
            nuevo_nombre = input("NOMBRE : ")
            nuevo_email = input("EMAIL : ")
            nuevo_celular = input("CELULAR : ")
            actualizar_alumno(alumno['id'],nuevo_nombre,nuevo_email,nuevo_celular)
            print("ALUMNO ACTUALIZADO CON EXITO...")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE EMAIL DEL ALUMNO A ELIMINAR :')
        alumno = buscar_alumno(valor_busqueda)
        if not alumno:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            eliminar_alumno(alumno['id'])
            print('ALUMNO ELIMINADO!!!')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)