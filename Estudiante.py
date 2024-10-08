from Persona import Persona

class Estudiante(Persona):
    """
    Clase que representa a un estudiante, hereda de la clase Persona.
    """
    contador_estudiantes = 0  # Contador de estudiantes creados

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, matricula: str, carrera: str, semestre: int):
        """
        Inicializa una nueva instancia de la clase Estudiante.

        """
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        Estudiante.contador_estudiantes += 1  # Incrementa el contador al crear un estudiante.

    # Getter y setter para 'matricula'
    @property
    def matricula(self):
        """
        Obtiene la matrícula del estudiante.

        Returns:
            str: La matrícula del estudiante.
        """
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        """
        Establece la matrícula del estudiante. Debe ser una cadena no vacía.

        Args:
            valor (str): Nueva matrícula.
        """
        if isinstance(valor, str) and valor.strip():
            self._matricula = valor

    # Getter y setter para 'carrera'
    @property
    def carrera(self):
        """
        Obtiene la carrera del estudiante.

        Returns:
            str: La carrera del estudiante.
        """
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        """
        Establece la carrera del estudiante. Debe ser una cadena no vacía.

        Args:
            valor (str): Nueva carrera.
        """
        if isinstance(valor, str) and valor.strip():
            self._carrera = valor

    # Getter y setter para 'semestre'
    @property
    def semestre(self):
        """
        Obtiene el semestre del estudiante.

        Returns:
            int: El semestre en el que está inscrito el estudiante.
        """
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        """
        Establece el semestre del estudiante. Debe ser un número entero mayor a 0.

        Args:
            valor (int): Nuevo semestre.
        """
        if isinstance(valor, int) and valor > 0:
            self._semestre = valor

    # Método de clase
    @classmethod
    def cantidad_estudiantes(cls):
        """
        Retorna la cantidad total de estudiantes creados.

        Returns:
            int: El número total de instancias de Estudiante creadas.
        """
        return cls.contador_estudiantes

    # Método para estudiar
    def estudiar(self, materia: str, horas: int):
        """
        Simula que el estudiante estudia una materia durante un tiempo determinado.

        Args:
            materia (str): Nombre de la materia que está estudiando.
            horas (int): Número de horas que estudiará la materia.
        """
        print(f"El estudiante {self.nombre} con matrícula {self.matricula} está estudiando {materia} durante {horas} horas.")

    # Método para presentarse
    def presentarse(self):
        """
        Muestra una presentación del estudiante, incluyendo su nombre, matrícula, carrera y semestre.
        """
        print(f"Hola, soy {self.nombre} {self.apellido}, estudiante de {self.carrera} en el semestre {self.semestre}. Mi matrícula es {self.matricula}.")