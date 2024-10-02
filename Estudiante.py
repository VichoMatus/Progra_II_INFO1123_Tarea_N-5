class Estudiante:
    contador_estudiantes = 0

    def __init__(self, matricula, carrera, semestre):
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre
        Estudiante.contador_estudiantes += 1

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__matricula = valor


    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__carrera = valor


    @property
    def semestre(self):
        return self.__semestre

    @semestre.setter
    def semestre(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__semestre = valor


    @staticmethod
    def cantidad_estudiantes():
        return Estudiante.contador_estudiantes

    def estudiar(self, materia, horas):
        print(f"El estudiante con matrícula {self.__matricula} está estudiando {materia} durante {horas} horas.")

    def presentarse(self):
        print(f"El estudiante con matrícula {self.__matricula} se está presentando.")
