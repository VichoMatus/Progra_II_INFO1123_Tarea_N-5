from Grupo import Grupo
from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante

class ProgramaAcademico:
    contador_programas = 0

    def __init__(self, nombre: str, codigo: str):
        self._nombre = nombre
        self._codigo = codigo
        self._grupos = []  
        ProgramaAcademico.contador_programas += 1

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str):
        if isinstance(valor, str) and valor.strip():
            self._codigo = valor

    @property
    def grupos(self):
        return self._grupos

    @classmethod
    def cantidad_programas(cls):
        return cls.contador_programas

    def agregar_grupo(self, grupo):
        if isinstance(grupo, Grupo):
            self._grupos.append(grupo)
        else:
            print("El grupo que intenta agregar no es válido.")

    def eliminar_grupo(self, numero_grupo: int):
        if not self._grupos:
            print("No hay grupos en este programa.")
            return

        grupo_a_eliminar = None
        for grupo in self._grupos:
            if grupo.numero_grupo == numero_grupo:
                grupo_a_eliminar = grupo
                break

        if grupo_a_eliminar:
            self._grupos.remove(grupo_a_eliminar)
            print(f"El grupo con número {numero_grupo} ha sido eliminado.")
        else:
            print(f"No se encontró un grupo con el número {numero_grupo}.")

    def mostrar_programa(self):
        print(f"Programa Académico: {self.nombre} (Código: {self.codigo})")
        if self._grupos:
            print("Grupos:")
            for grupo in self._grupos:
                grupo.mostrar_grupo()
        else:
            print("No hay grupos asociados a este programa.")
