from .empresa import Empresa

class Cliente(Empresa):
    
    def __init__(self,ruc,rs,dir,cred):
        super().__init__(ruc,rs,dir)
        self.linea_credito = cred
    
    def mostrar(self):
        print('*'*50 + "DATOS DEL CLIENTE")
        super().mostrar()
        print(f'LINEA DE CREDITO : {self.linea_credito}')