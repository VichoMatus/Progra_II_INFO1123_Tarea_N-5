from Persona     import Persona

class Profesor(Persona):
    contador_profesores = 0

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, numero_empleado: str, departamento: str):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento
        Profesor.contador_profesores += 1

    @property
    def numero_empleado(self):
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, numero_empleado: str):
        self._numero_empleado = numero_empleado

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: str):
        self._departamento = departamento

    @classmethod
    def cantidad_profesores(cls):
        return cls.contador_profesores

    def enseñar(self, materia: str):
        print(f"Estoy enseñando {materia} en el departamento de {self.departamento}")

    def presentarse(self):
        return f"Hola, soy el profesor {self.nombre} {self.apellido}, trabajo en el departamento de {self.departamento} con número de empleado {self.numero_empleado}."
