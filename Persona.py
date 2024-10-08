class Persona():
    """
    Clase base para representar a una persona con atributos básicos como nombre, apellido y fecha de nacimiento.
    """
    contador_personas = 0  # Contador de personas creadas

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str):
        """
        Inicializa una nueva instancia de la clase Persona.
        """
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        Persona.contador_personas += 1  # Incrementa el contador de personas

    # Getter y setter para 'nombre'
    @property
    def nombre(self):
        """
        Obtiene el nombre de la persona.

        Returns: El nombre de la persona.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """
        Establece el nombre de la persona.
        Args:
            nombre (str): Nuevo nombre de la persona.
        """
        self._nombre = nombre

    # Getter y setter para 'apellido'
    @property
    def apellido(self):
        """
        Obtiene el apellido de la persona.

        Returns:
            str: El apellido de la persona.
        """
        return self._apellido

    @apellido.setter
    def apellido(self, ape):
        """
        Establece el apellido de la persona.

        Args:
            ape (str): Nuevo apellido de la persona.
        """
        self._apellido = ape

    # Getter y setter para 'fecha_de_nacimiento'
    @property
    def fecha_de_nacimiento(self):
        """
        Obtiene la fecha de nacimiento de la persona.

        Returns:
            str: La fecha de nacimiento de la persona.
        """
        return self._fecha_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha):
        """
        Establece la fecha de nacimiento de la persona.

        Args:
            fecha (str): Nueva fecha de nacimiento de la persona.
        """
        self._fecha_nacimiento = fecha

    # Método de clase para obtener la cantidad de personas creadas
    @classmethod
    def cantidad_personas(cls):
        """
        Retorna la cantidad total de personas creadas.
        
        Returns:
            int: Número total de instancias de Persona creadas.
        """
        return cls.contador_personas

    # Método para presentarse
    def presentarse(self):
        """
        Muestra una presentación de la persona con su nombre, apellido y fecha de nacimiento.

        Returns:
            str: Un mensaje de presentación.
        """
        return f"Hola, me presento... mi nombre es {self.nombre} {self.apellido} y nací el {self.fecha_de_nacimiento}"

    


    
    
    