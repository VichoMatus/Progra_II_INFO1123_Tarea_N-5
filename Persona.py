class Persona():
    contador_personas = 0
    

    def __init__(self, nombre : str, apellido : str, fecha_nacimiento : str):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        Persona.contador_personas += 1
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, ape):
        self._apellido = ape
        
    @property
    def fecha_de_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha):
        self._fecha_nacimiento = fecha
    
    @classmethod
    def cantidad_personas(cls):
        return cls.contador_personas
    
    def presentarse(self):
        return f"Hola, me presento... mi nombre es {self.nombre} {self.apellido} y naci el {self.fecha_de_nacimiento}"
