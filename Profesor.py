from Persona import Persona

class Profesor(Persona):
    """
    Clase para representar a un profesor, que hereda de la clase Persona y tiene atributos adicionales como número de empleado y departamento.
    """
    contador_profesores = 0  # Contador de profesores creados

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, numero_empleado: str, departamento: str):
        """
        Inicializa una nueva instancia de la clase Profesor.
        """
        super().__init__(nombre, apellido, fecha_nacimiento)  # Llama al constructor de la clase base 'Persona'
        self._numero_empleado = numero_empleado
        self._departamento = departamento
        Profesor.contador_profesores += 1  # Incrementa el contador de profesores

    # Getter y setter para 'numero_empleado'
    @property
    def numero_empleado(self):
        """
        Obtiene el número de empleado del profesor.

        Return:
            str: El número de empleado del profesor.
        """
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, numero_empleado: str):
        """
        Establece el número de empleado del profesor.

        Args:
            numero_empleado (str): Nuevo número de empleado del profesor.
        """
        self._numero_empleado = numero_empleado

    # Getter y setter para 'departamento'
    @property
    def departamento(self):
        """
        Obtiene el departamento en el que trabaja el profesor.

        Return:
            str: El departamento del profesor.
        """
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: str):
        """
        Establece el departamento del profesor.

        Args:
            departamento (str): Nuevo departamento del profesor.
        """
        self._departamento = departamento

    # Método de clase para obtener la cantidad de profesores creados
    @classmethod
    def cantidad_profesores(cls):
        """
        Retorna la cantidad total de profesores creados.

        Return:
            int: Número total de instancias de Profesor creadas.
        """
        return cls.contador_profesores

    # Método para enseñar una materia
    def enseñar(self, materia: str):
        """
        Método que simula que el profesor está enseñando una materia.

        Args:
            materia (str): Nombre de la materia que el profesor está enseñando.
        """
        print(f"Estoy enseñando {materia} en el departamento de {self.departamento}")

    # Método para presentarse
    def presentarse(self):
        """
        Muestra una presentación del profesor con su nombre, apellido, departamento y número de empleado.

        Return:
            str: Un mensaje de presentación.
        """
        return f"Hola, soy el profesor {self.nombre} {self.apellido}, trabajo en el departamento de {self.departamento} con número de empleado {self.numero_empleado}."
