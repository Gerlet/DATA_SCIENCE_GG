import os
import tabulate
import time
from librerias.lib_alumnos import buscar_alumno,mostrar_menu,cargar_datos,grabar_datos

f = open('alumnos.txt','r')
str_alumnos = f.read()
f.close()

lista_alumnos = cargar_datos(str_alumnos)
ANCHO = 50
opcion = 0


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
        dic_nuevo_alumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        lista_alumnos.append(dic_nuevo_alumno)
        print(" ALUMNO REGISTRADO CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR ALUMNOS")
        print("="*ANCHO)
        cabeceras = ["NOMBRE","EMAIL","CELULAR"]
        tabla = [alumno.values() for alumno in lista_alumnos]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE EMAIL DEL ALUMNO A ACTUALIZAR :')
        posicion_busqueda = buscar_alumno(valor_busqueda,lista_alumnos)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            print(f' ALUMNO A ACTUALIZAR : {lista_alumnos[posicion_busqueda].get("nombre")}')
            nuevo_nombre = input("NOMBRE : ")
            nuevo_email = input("EMAIL : ")
            nuevo_celular = input("CELULAR : ")
            dic_actualizar_alumno = {
                'nombre':nuevo_nombre,
                'email':nuevo_email,
                'celular':nuevo_celular
            }
            lista_alumnos[posicion_busqueda] = dic_actualizar_alumno
            print("ALUMNO ACTUALIZADO CON EXITO...")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE EMAIL DEL ALUMNO A ELIMINAR :')
        posicion_busqueda = buscar_alumno(valor_busqueda,lista_alumnos)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            lista_alumnos.pop(posicion_busqueda)
            print('ALUMNO ELIMINADO!!!')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        str_alumnos = grabar_datos(lista_alumnos)
        fsalida = open('alumnos.txt','w')
        fsalida.write(str_alumnos)
        fsalida.close()
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)