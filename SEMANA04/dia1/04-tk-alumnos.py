from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector

class AlumnoTk:

    def __init__(self,app):
        self.app = app
        self.app.title('Alumnos')
        self.app.geometry('640x480')

        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='db_codigo'
        )

        self.cursor = self.db.cursor()

        frame = LabelFrame(self.app,text='Nuevo Alumno')
        frame.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

        lb_nombre = Label(frame,text='Nombre : ')
        lb_nombre.grid(row=1,column=0)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=1,column=1)

        lb_email = Label(frame,text='Email : ')
        lb_email.grid(row=2,column=0)
        self.txt_email = Entry(frame)
        self.txt_email.grid(row=2,column=1)

        lb_celular = Label(frame,text='Celular : ')
        lb_celular.grid(row=3,column=0)
        self.txt_celular = Entry(frame)
        self.txt_celular.grid(row=3,column=1) 

        btn_insertar = Button(frame,text='Insertar Alumno',command=self.insertar)
        btn_insertar.grid(row=4,column=1,columnspan=2)

        #grilla de alumnos
        self.tree = Treeview(self.app)
        self.tree['columns'] = ('Nombre','Email','Celular')

        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column('Nombre')
        self.tree.column('Email')
        self.tree.column('Celular')

        self.tree.heading('#0',text='id')
        self.tree.heading('Nombre',text='Nombre')
        self.tree.heading('Email',text='Email')
        self.tree.heading('Celular',text='Celular')

        self.tree.grid(row=5,column=0,padx=20,pady=20)
        self.cargar_alumnos()

    def cargar_alumnos(self):
        #limpiar el treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        #cargar alumnos
        self.cursor.execute("select id,nombre,email,celular from tbl_alumno")
        for row in self.cursor.fetchall():
            self.tree.insert('',END,iid=row[0],values=row[1:])

    def insertar(self):
        nuevo_alumno = (
            self.txt_nombre.get(),
            self.txt_email.get(),
            self.txt_celular.get()
        )
        query = "insert into tbl_alumno(nombre,email,celular) values(%s,%s,%s)"
        self.cursor.execute(query,nuevo_alumno)
        self.db.commit()
        self.cargar_alumnos()

if __name__ == "__main__":
    app = Tk()
    app_alumno = AlumnoTk(app)
    app.mainloop()