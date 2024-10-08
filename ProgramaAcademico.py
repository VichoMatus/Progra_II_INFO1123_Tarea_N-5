from Grupo import Grupo
from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante

class ProgramaAcademico:
    """
    Clase que representa un programa académico en una universidad, el cual tiene varios grupos.
    """
    contador_programas = 0  # Contador de programas académicos creados

    def __init__(self, nombre: str, codigo: str):
        """
        Inicializa una nueva instancia de ProgramaAcademico.
        """
        self._nombre = nombre
        self._codigo = codigo
        self._grupos = []  # Lista vacía para almacenar los grupos
        ProgramaAcademico.contador_programas += 1  # Incrementa el contador de programas

    # Getter y setter para 'nombre'
    @property
    def nombre(self):
        """
        Obtiene el nombre del programa académico.

        Return:
            str: El nombre del programa académico.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        """
        Establece el nombre del programa académico si es una cadena válida.

        Args:
            valor (str): Nuevo nombre del programa académico.
        """
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor

    # Getter y setter para 'codigo'
    @property
    def codigo(self):
        """
        Obtiene el código del programa académico.

        Return:
            str: El código del programa académico.
        """
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str):
        """
        Establece el código del programa académico si es una cadena válida.

        Args:
            valor (str): Nuevo código del programa académico.
        """
        if isinstance(valor, str) and valor.strip():
            self._codigo = valor

    # Getter para la lista de grupos
    @property
    def grupos(self):
        """
        Obtiene la lista de grupos asociados al programa académico.

        Return:
            list: Lista de objetos Grupo.
        """
        return self._grupos

    # Método de clase para obtener la cantidad de programas académicos
    @classmethod
    def cantidad_programas(cls):
        """
        Retorna la cantidad total de programas académicos creados.

        Return:
            int: Número total de instancias de ProgramaAcademico creadas.
        """
        return cls.contador_programas

    # Método para agregar un grupo al programa
    def agregar_grupo(self, grupo):
        """
        Agrega un grupo al programa académico si el objeto es una instancia de Grupo.

        Args:
            grupo (Grupo): El grupo que se desea agregar.
        """
        if isinstance(grupo, Grupo):
            self._grupos.append(grupo)
        else:
            print("El grupo que intenta agregar no es válido.")

    # Método para eliminar un grupo del programa
    def eliminar_grupo(self, numero_grupo: int):
        """
        Elimina un grupo del programa académico por su número de grupo.

        Args:
            numero_grupo (int): El número del grupo que se desea eliminar.
        """
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

    # Método para mostrar información sobre el programa académico y sus grupos
    def mostrar_programa(self):
        """
        Muestra la información del programa académico y la lista de grupos asociados.

        Si no hay grupos asociados, indica que no hay grupos disponibles.
        """
        print(f"Programa Académico: {self.nombre} (Código: {self.codigo})")
        if self._grupos:
            print("Grupos:")
            for grupo in self._grupos:
                grupo.mostrar_grupo()
        else:
            print("No hay grupos asociados a este programa.")
