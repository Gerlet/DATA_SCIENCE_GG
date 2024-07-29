"""from models.proveedor import Proveedor
from models.cliente import Cliente
from dao.clientedao import ClienteDAO

cliente1 = Cliente('10','cliente sac','calle girasoles 123',5000)
proveedor1 = Proveedor('20','PROVEEDOR MULTINACIONAL','inter 123','CESAR')
cliente1.mostrar()
proveedor1.mostrar()

dao_cliente = ClienteDAO()
dao_cliente.insertar(cliente1)
print("cliente registrado")"""
from tkinter import *
from tkviews.clientetk import ClienteTk

if __name__ == "__main__":
    app = Tk()
    app_cliente = ClienteTk(app)
    app.mainloop()


