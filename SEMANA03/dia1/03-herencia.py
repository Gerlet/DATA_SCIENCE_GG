class Persona:

    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema

    def mostrar(self):
        print("*"*50)
        print(f"NOMBRE : {self.nombre}")
        print(f"EMAIL : {self.email}")

class Alumno(Persona):

    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota = nota
    
class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp


alumno1 = Alumno('CESAR','cesar@gmail.com',15)
alumno1.mostrar()
print(f"NOTA : {alumno1.nota}")

profesor1 = Profesor('GUILLERMO','guille@gmail.com','BASE DE DATOS')
profesor1.mostrar()
print(f"ESPECIALIDAD : {profesor1.especialidad}")