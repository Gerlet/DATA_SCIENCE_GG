
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

def buscar_alumno(valor_busqueda,lista_alumnos):
    posicion_busqueda = -1
    for posicion in range(len(lista_alumnos)):
        dic_alumno = lista_alumnos[posicion]
        if valor_busqueda in dic_alumno.values():
            posicion_busqueda = posicion
            break
    return posicion_busqueda

def cargar_datos(str_datos):
    lista_alumnos = []
    lista_general = str_datos.splitlines()
    for str_registro in lista_general:
        lista_registro = str_registro.split(',')
        dic_registro = {
        'nombre':lista_registro[0],
        'email':lista_registro[1],
        'celular':lista_registro[2]
        }
        lista_alumnos.append(dic_registro)
    return lista_alumnos

def grabar_datos(lista_alumnos):
    str_alumnos = ""
    for dic_registro in lista_alumnos:
        for clave,valor in dic_registro.items():
            str_alumnos += valor
            if clave != 'celular':
                str_alumnos += ','
            else:
                str_alumnos += '\n'
    
    return str_alumnos

