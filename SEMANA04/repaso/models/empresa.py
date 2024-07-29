class Empresa:
    def __init__(self,ruc,rs,dir):
        self.ruc = ruc
        self.razon_social = rs
        self.direccion = dir

    def mostrar(self):
        print(f"RUC : {self.ruc}")
        print(f"RAZON SOCIAL : {self.razon_social}")
        print(f"DIRECCIÓN :{self.direccion} ")