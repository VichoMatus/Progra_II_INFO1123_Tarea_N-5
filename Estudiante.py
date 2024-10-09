from Persona import Persona

class Estudiante(Persona):
    contador_estudiantes = 0

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, matricula: str, carrera: str, semestre: int):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.matricula = matricula  # Utiliza el setter
        self.carrera = carrera       # Utiliza el setter
        self.semestre = semestre     # Utiliza el setter
        Estudiante.contador_estudiantes += 1

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._matricula = valor
        else:
            raise ValueError("La matrícula debe ser una cadena no vacía.")

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._carrera = valor
        else:
            raise ValueError("La carrera debe ser una cadena no vacía.")

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._semestre = valor
        else:
            raise ValueError("El semestre debe ser un entero positivo.")

    @classmethod
    def cantidad_estudiantes(cls):
        return cls.contador_estudiantes

    def estudiar(self, materia: str, horas: int):
        if horas > 0:
            print(f"El estudiante {self.nombre} con matrícula {self.matricula} está estudiando {materia} durante {horas} horas.")
        else:
            print("Las horas de estudio deben ser un número positivo.")

    def presentarse(self):
        return (f"Hola, soy {self.nombre} {self.apellido}, "
                f"estudiante de {self.carrera} en el semestre {self.semestre}. "
                f"Mi matrícula es {self.matricula}.")
