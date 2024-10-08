from Profesor import Profesor
from Estudiante import Estudiante
from Asignatura import Asignatura

class Grupo:
    """
    Clase que representa un grupo de estudiantes en una asignatura con un profesor asignado.
    """
    contador_grupos = 0  # Contador de grupos creados

    def __init__(self, numero_grupo: int, asignatura: Asignatura, profesor: Profesor):
        """
        Inicializa una nueva instancia de la clase Grupo.
        """
        self._numero_grupo = numero_grupo
        self._asignatura = asignatura
        self._profesor = profesor
        self._estudiantes = []  # Lista vacía para los estudiantes
        Grupo.contador_grupos += 1  # Incrementa el contador de grupos al crear uno nuevo.

    # Getter y setter para 'numero_grupo'
    @property
    def numero_grupo(self):
        """
        Obtiene el número del grupo.

        Returns:
            int: Número del grupo.
        """
        return self._numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, valor: int):
        """
        Establece el número del grupo. Debe ser un valor entero mayor que 0.

        Args:
            valor (int): Nuevo número de grupo.
        """
        if isinstance(valor, int) and valor > 0:
            self._numero_grupo = valor

    # Getter y setter para 'asignatura'
    @property
    def asignatura(self):
        """
        Obtiene la asignatura del grupo.

        Returns:
            Asignatura: La asignatura que se imparte en el grupo.
        """
        return self._asignatura

    @asignatura.setter
    def asignatura(self, valor):
        """
        Establece la asignatura del grupo.

        Args:
            valor (Asignatura): Nueva asignatura para el grupo.
        """
        self._asignatura = valor

    # Getter y setter para 'profesor'
    @property
    def profesor(self):
        """
        Obtiene el profesor asignado al grupo.

        Returns:
            Profesor: El profesor que imparte el grupo.
        """
        return self._profesor

    @profesor.setter
    def profesor(self, valor):
        """
        Establece el profesor asignado al grupo.

        Args:
            valor (Profesor): Nuevo profesor para el grupo.
        """
        self._profesor = valor

    # Getter para 'estudiantes'
    @property
    def estudiantes(self):
        """
        Obtiene la lista de estudiantes del grupo.

        Returns:
            list: Lista de estudiantes asignados al grupo.
        """
        return self._estudiantes

    # Método de clase para obtener la cantidad de grupos creados
    @classmethod
    def cantidad_grupos(cls):
        """
        Retorna la cantidad total de grupos creados.

        Returns:
            int: Número total de instancias de Grupo creadas.
        """
        return cls.contador_grupos

    # Método para agregar un estudiante al grupo
    def agregar_estudiante(self, estudiante):
        """
        Agrega un estudiante al grupo si no está ya presente.

        Args:
            estudiante (Estudiante): Estudiante que se quiere agregar al grupo.
        """
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)

    # Método para eliminar un estudiante del grupo por matrícula
    def eliminar_estudiante(self, matricula: str):
        """
        Elimina un estudiante del grupo utilizando su matrícula.

        Args:
            matricula (str): Matrícula del estudiante a eliminar.
        """
        self._estudiantes = [est for est in self._estudiantes if est.matricula != matricula]

    # Método para mostrar la información del grupo
    def mostrar_grupo(self):
        """
        Muestra la información del grupo, incluyendo el número de grupo, asignatura,
        profesor y estudiantes asignados.

        Muestra por consola los datos del grupo.
        """
        print(f"Grupo {self.numero_grupo}:")
        print(f"Asignatura: {self.asignatura.nombre}")
        print(f"Profesor: {self.profesor.nombre} {self.profesor.apellido}")
        print(f"Estudiantes:")
        for estudiante in self._estudiantes:
            print(f"- {estudiante.nombre} {estudiante.apellido} (Matrícula: {estudiante.matricula})")
