from .empresa import Empresa

class Proveedor(Empresa):
    def __init__(self,ruc,rs,dir,cont):
        super().__init__(ruc,rs,dir)
        self.contacto = cont
    
    def mostrar(self):
        print('*'*50 + "DATOS DEL PROVEEDOR")
        super().mostrar()
        print(f'PERSONA DE CONTACTO : {self.contacto}')
