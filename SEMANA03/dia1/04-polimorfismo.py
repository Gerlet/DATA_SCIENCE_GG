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

    def mostrar(self):
        super().mostrar()
        print(f"NOTA : {self.nota}")
    
class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp

    def mostrar(self):
        super().mostrar()
        print(f"ESPECIALIDAD : {self.especialidad}")

class Empleado(Persona):
    pass


alumno1 = Alumno('CESAR','cesar@gmail.com',15)
alumno1.mostrar()

profesor1 = Profesor('GUILLERMO','guille@gmail.com','BASE DE DATOS')
profesor1.mostrar()

empleado1 = Empleado('ANA','ana@gmail.com')
empleado1.mostrar()