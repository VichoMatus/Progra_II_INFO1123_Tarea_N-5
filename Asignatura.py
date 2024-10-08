class Asignatura:
    _contador_asignaturas = 0  # Atributo de clase para contar la cantidad de asignaturas creadas.

    def __init__(self, nombre: str, codigo: str, creditos: int):
        """
        Inicializa una nueva instancia de la clase Asignatura.
        """
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos
        Asignatura._contador_asignaturas += 1  # Incrementa el contador al crear una nueva asignatura.

    # Getter y setter para el atributo 'nombre'
    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre de la asignatura.

        Returns:
            str: El nombre de la asignatura.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la asignatura.

        Args:
            nombre (str): El nuevo nombre de la asignatura.
        """
        self._nombre = nombre

    # Getter y setter para el atributo 'codigo'
    @property
    def codigo(self) -> str:
        """
        Obtiene el código de la asignatura.

        Returns:
            str: El código de la asignatura.
        """
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo: str) -> None:
        """
        Establece el código de la asignatura.

        Args:
            codigo (str): El nuevo código de la asignatura.
        """
        self._codigo = codigo

    # Getter y setter para el atributo 'creditos'
    @property
    def creditos(self) -> int:
        """
        Obtiene los créditos de la asignatura.

        Returns:
            int: El número de créditos de la asignatura.
        """
        return self._creditos
 
    @creditos.setter
    def creditos(self, creditos: int) -> None:
        """
        Establece los créditos de la asignatura.

        Args:
            creditos (int): La nueva cantidad de créditos de la asignatura.
        """
        self._creditos = creditos

    # Método de clase
    @classmethod
    def cantidad_asignaturas(cls) -> int:
        """
        Devuelve la cantidad total de asignaturas creadas.

        Returns:
            int: El número de asignaturas creadas.
        """
        return cls._contador_asignaturas

    # Método para mostrar información de la asignatura
    def mostrar_informacion(self) -> None:
        
       # Muestra la información de la asignatura (nombre, código y créditos) en la consola.
        print(f"Nombre: {self._nombre}")
        print(f"Código: {self._codigo}")
        print(f"Créditos: {self._creditos}")