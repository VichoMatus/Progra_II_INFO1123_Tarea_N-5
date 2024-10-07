import tkinter as tk
from tkinter import messagebox, simpledialog
from ProgramaAcademico import ProgramaAcademico
from Profesor import Profesor
from Estudiante import Estudiante
from Asignatura import Asignatura
from Grupo import Grupo

class AcademicManagerApp:
    """Clase para la gestión académica a través de una interfaz de usuario."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión Académica")
        
        self.programa_academico = ProgramaAcademico("Programa de Ingeniería", "ING123")

        self.create_widgets()

    def create_widgets(self):
        """Crear botones para la gestión académica."""
        actions = [
            ("Crear Profesor", self.crear_profesor),
            ("Crear Estudiante", self.crear_estudiante),
            ("Crear Asignatura", self.crear_asignatura),
            ("Crear Grupo", self.crear_grupo),
            ("Asignar Estudiante a Grupo", self.asignar_estudiante_a_grupo),
            ("Mostrar Información", self.mostrar_informacion)
        ]

        for text, command in actions:
            button = tk.Button(self.master, text=text, command=command)
            button.pack(pady=5)

    def crear_profesor(self):
        """Crear un nuevo profesor."""
        try:
            nombre = self.get_input("Nombre del profesor")
            apellido = self.get_input("Apellido del profesor")
            fecha_nacimiento = self.get_input("Fecha de nacimiento")
            numero_empleado = self.get_input("Número de empleado")
            departamento = self.get_input("Departamento")

            nuevo_profesor = Profesor(nombre, apellido, fecha_nacimiento, numero_empleado, departamento)
            messagebox.showinfo("Éxito", "Profesor creado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def crear_estudiante(self):
        """Crear un nuevo estudiante."""
        try:
            nombre = self.get_input("Nombre del estudiante")
            apellido = self.get_input("Apellido del estudiante")
            fecha_nacimiento = self.get_input("Fecha de nacimiento")
            matricula = self.get_input("Matrícula")
            carrera = self.get_input("Carrera")
            semestre = self.get_integer_input("Semestre")

            nuevo_estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
            messagebox.showinfo("Éxito", "Estudiante creado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def crear_asignatura(self):
        """Crear una nueva asignatura."""
        try:
            nombre = self.get_input("Nombre de la asignatura")
            codigo = self.get_input("Código de la asignatura")
            creditos = self.get_integer_input("Créditos")

            nueva_asignatura = Asignatura(nombre, codigo, creditos)
            messagebox.showinfo("Éxito", "Asignatura creada exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def crear_grupo(self):
        """Crear un nuevo grupo."""
        try:
            numero_grupo = self.get_integer_input("Número del grupo")
            codigo_asignatura = self.get_input("Código de la asignatura")
            nombre_profesor = self.get_input("Nombre del profesor")

            asignatura = Asignatura(codigo_asignatura, "Asignatura de Ejemplo", 5)
            profesor = Profesor(nombre_profesor, "Apellido", "01-01-1980", "P001", "Ciencias")

            nuevo_grupo = Grupo(numero_grupo, asignatura, profesor)
            self.programa_academico.agregar_grupo(nuevo_grupo)
            messagebox.showinfo("Éxito", "Grupo creado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def asignar_estudiante_a_grupo(self):
        """Asignar un estudiante a un grupo específico."""
        try:
            matricula = self.get_input("Matrícula del estudiante")
            numero_grupo = self.get_integer_input("Número del grupo")
            
            estudiante = Estudiante("Nombre Estudiante", "Apellido", "01-01-2000", matricula, "Ingeniería", 2)
            grupo = Grupo(numero_grupo, Asignatura("Asignatura", "ASG001", 5), Profesor("Nombre", "Apellido", "01-01-1980", "P001", "Ciencias"))
            
            grupo.agregar_estudiante(estudiante)
            messagebox.showinfo("Éxito", "Estudiante asignado al grupo exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_informacion(self):
        """Mostrar información detallada sobre el programa académico."""
        info = self.programa_academico.mostrar_programa()
        messagebox.showinfo("Información del Programa Académico", info)

    def get_input(self, prompt):
        """Obtener entrada de texto del usuario."""
        result = simpledialog.askstring("Entrada", prompt)
        if result is None or result.strip() == "":
            raise ValueError(f"La entrada para '{prompt}' no puede estar vacía.")
        return result.strip()

    def get_integer_input(self, prompt):
        """Obtener entrada de número entero del usuario."""
        result = simpledialog.askinteger("Entrada", prompt)
        if result is None or result <= 0:
            raise ValueError(f"La entrada para '{prompt}' debe ser un entero positivo.")
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = AcademicManagerApp(root)
    root.mainloop()
