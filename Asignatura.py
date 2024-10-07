class Asignatura:
    _contador_asignaturas = 0

    def __init__(self, nombre: str, codigo: str, creditos: int):
        self.nombre = nombre   # Utiliza el setter para validación
        self.codigo = codigo    # Utiliza el setter para validación
        self.creditos = creditos  # Utiliza el setter para validación
        Asignatura._contador_asignaturas += 1

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: str) -> None:
        if isinstance(codigo, str) and codigo.strip():
            self._codigo = codigo
        else:
            raise ValueError("El código debe ser una cadena no vacía.")

    @property
    def creditos(self) -> int:
        return self._creditos

    @creditos.setter
    def creditos(self, creditos: int) -> None:
        if isinstance(creditos, int) and creditos > 0:
            self._creditos = creditos
        else:
            raise ValueError("Los créditos deben ser un entero positivo.")

    @classmethod
    def cantidad_asignaturas(cls) -> int:
        return cls._contador_asignaturas

    def mostrar_informacion(self) -> str:
        return (f"Nombre: {self.nombre}\n"
                f"Código: {self.codigo}\n"
                f"Créditos: {self.creditos}")
