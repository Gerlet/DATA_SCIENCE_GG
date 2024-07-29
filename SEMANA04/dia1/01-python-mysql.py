import mysql.connector

connection = mysql.connector.connect(user='root',password='root',host='localhost',database='db_codigo')

print("estas conectado a la base de datos")

alumnos_cursor = connection.cursor()

#alumnos_cursor.execute("insert into tbl_alumno(nombre,email,celular) values('Ana','ana@gmail.com','77777')")
#connection.commit()
#print("alumno insertado")

alumnos_cursor.execute("select * from tbl_alumno")
resultado = alumnos_cursor.fetchall()
print(resultado)
for registro in resultado:
    print('*'*50)
    print(f'NOMBRE : {registro[1]}')
    print(f'EMAIL : {registro[2]}')

connection.close()