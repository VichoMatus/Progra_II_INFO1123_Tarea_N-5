from Profesor import Profesor
from Estudiante import Estudiante
from Asignatura import Asignatura

class Grupo:
    contador_grupos = 0

    def __init__(self, numero_grupo: int, asignatura : Asignatura, profesor : Profesor):
        self._numero_grupo = numero_grupo
        self._asignatura = asignatura
        self._profesor = profesor
        self._estudiantes = [Estudiante]
        Grupo.contador_grupos += 1

    @property
    def numero_grupo(self):     
        return self._numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            self._numero_grupo = valor

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, valor):
        self._asignatura = valor

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, valor):
        self._profesor = valor

    @property
    def estudiantes(self):
        return self._estudiantes

    @classmethod
    def cantidad_grupos(cls):
        return cls.contador_grupos

    def agregar_estudiante(self, estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)

    def eliminar_estudiante(self, matricula: str):
        self._estudiantes = [est for est in self._estudiantes if est.matricula != matricula]

    def mostrar_grupo(self):
        print(f"Grupo {self.numero_grupo}:")
        print(f"  Asignatura: {self.asignatura.nombre}")
        print(f"  Profesor: {self.profesor.nombre} {self.profesor.apellido}")
        print(f"  Estudiantes:")
        for estudiante in self._estudiantes:
            print(f"    - {estudiante.nombre} {estudiante.apellido} (Matrícula: {estudiante.matricula})")
