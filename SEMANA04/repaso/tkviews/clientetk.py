from tkinter import *
from tkinter.ttk import Treeview
from dao.clientedao import ClienteDAO
from models.cliente import Cliente

class ClienteTk:

    def __init__(self,app):
        self.app = app
        self.app.title('Clientes')
        self.app.geometry('640x480')

        frame = LabelFrame(self.app,text='Nuevo Cliente')
        frame.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

        lb_razon_social = Label(frame,text='Razon Social : ')
        lb_razon_social.grid(row=1,column=0)
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=1,column=1)

        lb_ruc = Label(frame,text='RUC : ')
        lb_ruc.grid(row=2,column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=2,column=1)

        lb_direccion = Label(frame,text='Dirección : ')
        lb_direccion.grid(row=3,column=0)
        self.txt_direccion = Entry(frame)
        self.txt_direccion.grid(row=3,column=1) 

        btn_insertar = Button(frame,text='Insertar Cliente',command=self.insertar)
        btn_insertar.grid(row=4,column=1,columnspan=2)

        #grilla de alumnos
        self.tree = Treeview(self.app)
        self.tree['columns'] = ('Razon Social','RUC','Direccion')

        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column('Razon Social')
        self.tree.column('RUC')
        self.tree.column('Direccion')

        self.tree.heading('#0',text='id')
        self.tree.heading('Razon Social',text='Razon Social')
        self.tree.heading('RUC',text='RUC')
        self.tree.heading('Direccion',text='Direccion')

        self.tree.grid(row=5,column=0,padx=20,pady=20)
        self.cargar_datos()

    def cargar_datos(self):
        #limpiar el treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        #cargar datos
        cliente_dao = ClienteDAO() 
        for row in cliente_dao.consultar():
            self.tree.insert('',END,iid=row[0],values=row[1:])

    def insertar(self):
        nuevo_cliente = Cliente(self.txt_ruc.get(),
                                self.txt_razon_social.get(),
                                self.txt_direccion.get(),
                                0)
        cliente_dao = ClienteDAO()
        cliente_dao.insertar(nuevo_cliente)
        self.cargar_datos()