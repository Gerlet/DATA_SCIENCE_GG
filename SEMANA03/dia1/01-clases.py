class Automovil:
    #atributos
    def __init__(self,aa,pl,col,mar):
        self.anio = aa
        self.placa = pl
        self.color = col
        self.marca = mar

    def encender(self):
        print('encender ' + self.marca)

# objectos
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
vw.encender()

tico = Automovil(1990,'CH-5678','Rojo','Daewo')
tico.encender()