class AlumnoDAO:
    def __init__(self):
        self.lista_alumnos = []

    def registrar_alumno(self,alumno):
        self.lista_alumnos.append(alumno)

    def mostrar_alumnos(self):
        return self.lista_alumnos

    def actualizar_alumno(self,nuevo_alumno,index):
        self.lista_alumnos[index] = nuevo_alumno

    def eliminar_alumno(self,index):
        del self.lista_alumnos[index]