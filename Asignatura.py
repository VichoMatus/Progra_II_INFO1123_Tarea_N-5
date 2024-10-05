class Asignatura:

    _contador_asignaturas = 0

    def __init__(self, nombre: str, codigo: str, creditos: int):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos
        Asignatura._contador_asignaturas += 1

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def codigo(self) -> str:
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo: str) -> None:
        self._codigo = codigo

    @property
    def creditos(self) -> int:
        return self._creditos
 
    @creditos.setter
    def creditos(self, creditos: int) -> None:
        self._creditos = creditos

    @classmethod
    def cantidad_asignaturas(cls) -> int:
        return cls._contador_asignaturas

    def mostrar_informacion(self) -> None:
        print(f"Nombre: {self._nombre}")
        print(f"Código: {self._codigo}")
        print(f"Créditos: {self._creditos}")


