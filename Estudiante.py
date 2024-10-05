from Persona import Persona

class Estudiante(Persona):
    contador_estudiantes = 0

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, matricula: str, carrera: str, semestre: int):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        Estudiante.contador_estudiantes += 1

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._matricula = valor

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._carrera = valor

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._semestre = valor

    @classmethod
    def cantidad_estudiantes(cls):
        return cls.contador_estudiantes

    def estudiar(self, materia: str, horas: int):
        print(f"El estudiante {self.nombre} con matrícula {self.matricula} está estudiando {materia} durante {horas} horas.")

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido}, estudiante de {self.carrera} en el semestre {self.semestre}. Mi matrícula es {self.matricula}.")

