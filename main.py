import customtkinter as ctk
from tkinter import ttk, messagebox

from Profesor import Profesor
from Estudiante import Estudiante
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Interfaz Académica")
        self.geometry("800x600")

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(expand=True, fill="both")

        self.crear_pestaña_profesor()
        self.crear_pestaña_estudiante()
        self.crear_pestaña_asignatura()
        self.crear_pestaña_grupo()
        self.crear_pestaña_programa_academico()

    def crear_pestaña_profesor(self):
        pestaña = self.tabview.add("Profesor")

        frame_metodos = ctk.CTkFrame(pestaña)
        frame_metodos.pack(side="left", padx=10, pady=10, fill="y")

        frame_datos = ctk.CTkFrame(pestaña)
        frame_datos.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.treeview_profesor = ttk.Treeview(frame_datos, columns=("nombre", "apellido", "departamento"), show="headings")
        self.treeview_profesor.pack(expand=True, fill="both")

        self.treeview_profesor.heading("nombre", text="Nombre")
        self.treeview_profesor.heading("apellido", text="Apellido")
        self.treeview_profesor.heading("departamento", text="Departamento")

        self.entry_nombre_profesor = ctk.CTkEntry(frame_metodos, placeholder_text="Nombre")
        self.entry_nombre_profesor.pack(padx=5, pady=5)

        self.entry_apellido_profesor = ctk.CTkEntry(frame_metodos, placeholder_text="Apellido")
        self.entry_apellido_profesor.pack(padx=5, pady=5)

        self.entry_departamento_profesor = ctk.CTkEntry(frame_metodos, placeholder_text="Departamento")
        self.entry_departamento_profesor.pack(padx=5, pady=5)

        boton_agregar = ctk.CTkButton(frame_metodos, text="Añadir Profesor", command=self.agregar_profesor)
        boton_agregar.pack(padx=5, pady=5)

        boton_eliminar = ctk.CTkButton(frame_metodos, text="Eliminar Profesor", command=self.eliminar_profesor)
        boton_eliminar.pack(padx=5, pady=5)

        boton_modificar = ctk.CTkButton(frame_metodos, text="Modificar Profesor", command=self.modificar_profesor)
        boton_modificar.pack(padx=5, pady=5)

    def agregar_profesor(self):
        nombre = self.entry_nombre_profesor.get().strip()
        apellido = self.entry_apellido_profesor.get().strip()
        departamento = self.entry_departamento_profesor.get().strip()

        if not nombre or not apellido or not departamento:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        elif not nombre.isalpha() or not apellido.isalpha():
            messagebox.showerror("Error", "Nombre y Apellido deben contener solo letras")
        else:
            self.treeview_profesor.insert("", "end", values=(nombre, apellido, departamento))

    def eliminar_profesor(self):
        selected_item = self.treeview_profesor.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un profesor para eliminar.")
            return
        self.treeview_profesor.delete(selected_item)

    def modificar_profesor(self):
        selected_item = self.treeview_profesor.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un profesor para modificar.")
            return

        values = self.treeview_profesor.item(selected_item)["values"]
        self.entry_nombre_profesor.insert(0, values[0])
        self.entry_apellido_profesor.insert(0, values[1])
        self.entry_departamento_profesor.insert(0, values[2])

        # Eliminar el profesor seleccionado
        self.eliminar_profesor()

    def crear_pestaña_estudiante(self):
        pestaña = self.tabview.add("Estudiante")

        frame_metodos = ctk.CTkFrame(pestaña)
        frame_metodos.pack(side="left", padx=10, pady=10, fill="y")

        frame_datos = ctk.CTkFrame(pestaña)
        frame_datos.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.treeview_estudiante = ttk.Treeview(frame_datos, columns=("nombre", "apellido", "matricula", "carrera", "semestre"), show="headings")
        self.treeview_estudiante.pack(expand=True, fill="both")

        self.treeview_estudiante.heading("nombre", text="Nombre")
        self.treeview_estudiante.heading("apellido", text="Apellido")
        self.treeview_estudiante.heading("matricula", text="Matrícula")
        self.treeview_estudiante.heading("carrera", text="Carrera")
        self.treeview_estudiante.heading("semestre", text="Semestre")

        self.entry_nombre_estudiante = ctk.CTkEntry(frame_metodos, placeholder_text="Nombre")
        self.entry_nombre_estudiante.pack(padx=5, pady=5)

        self.entry_apellido_estudiante = ctk.CTkEntry(frame_metodos, placeholder_text="Apellido")
        self.entry_apellido_estudiante.pack(padx=5, pady=5)

        self.entry_matricula_estudiante = ctk.CTkEntry(frame_metodos, placeholder_text="Matrícula")
        self.entry_matricula_estudiante.pack(padx=5, pady=5)

        self.entry_carrera_estudiante = ctk.CTkEntry(frame_metodos, placeholder_text="Carrera")
        self.entry_carrera_estudiante.pack(padx=5, pady=5)

        self.entry_semestre_estudiante = ctk.CTkEntry(frame_metodos, placeholder_text="Semestre")
        self.entry_semestre_estudiante.pack(padx=5, pady=5)

        boton_agregar = ctk.CTkButton(frame_metodos, text="Añadir Estudiante", command=self.agregar_estudiante)
        boton_agregar.pack(padx=5, pady=5)

        boton_eliminar = ctk.CTkButton(frame_metodos, text="Eliminar Estudiante", command=self.eliminar_estudiante)
        boton_eliminar.pack(padx=5, pady=5)

        boton_modificar = ctk.CTkButton(frame_metodos, text="Modificar Estudiante", command=self.modificar_estudiante)
        boton_modificar.pack(padx=5, pady=5)

    def agregar_estudiante(self):
        nombre = self.entry_nombre_estudiante.get().strip()
        apellido = self.entry_apellido_estudiante.get().strip()
        matricula = self.entry_matricula_estudiante.get().strip()
        carrera = self.entry_carrera_estudiante.get().strip()
        semestre = self.entry_semestre_estudiante.get().strip()

        if not nombre or not apellido or not matricula or not carrera or not semestre:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        elif not matricula.isdigit():
            messagebox.showerror("Error", "La matrícula debe ser numérica")
        elif not semestre.isdigit() or int(semestre) <= 0:
            messagebox.showerror("Error", "El semestre debe ser un número positivo")
        elif not nombre.isalpha() or not apellido.isalpha():
            messagebox.showerror("Error", "Nombre y Apellido deben contener solo letras")
        else:
            self.treeview_estudiante.insert("", "end", values=(nombre, apellido, matricula, carrera, semestre))

    def eliminar_estudiante(self):
        selected_item = self.treeview_estudiante.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un estudiante para eliminar.")
            return
        self.treeview_estudiante.delete(selected_item)

    def modificar_estudiante(self):
        selected_item = self.treeview_estudiante.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un estudiante para modificar.")
            return

        values = self.treeview_estudiante.item(selected_item)["values"]
        self.entry_nombre_estudiante.insert(0, values[0])
        self.entry_apellido_estudiante.insert(0, values[1])
        self.entry_matricula_estudiante.insert(0, values[2])
        self.entry_carrera_estudiante.insert(0, values[3])
        self.entry_semestre_estudiante.insert(0, values[4])

        # Eliminar el estudiante seleccionado
        self.eliminar_estudiante()

    def crear_pestaña_asignatura(self):
        pestaña = self.tabview.add("Asignatura")

        frame_metodos = ctk.CTkFrame(pestaña)
        frame_metodos.pack(side="left", padx=10, pady=10, fill="y")

        frame_datos = ctk.CTkFrame(pestaña)
        frame_datos.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.treeview_asignatura = ttk.Treeview(frame_datos, columns=("nombre", "codigo", "creditos"), show="headings")
        self.treeview_asignatura.pack(expand=True, fill="both")

        self.treeview_asignatura.heading("nombre", text="Nombre")
        self.treeview_asignatura.heading("codigo", text="Código")
        self.treeview_asignatura.heading("creditos", text="Créditos")

        self.entry_nombre_asignatura = ctk.CTkEntry(frame_metodos, placeholder_text="Nombre")
        self.entry_nombre_asignatura.pack(padx=5, pady=5)

        self.entry_codigo_asignatura = ctk.CTkEntry(frame_metodos, placeholder_text="Código")
        self.entry_codigo_asignatura.pack(padx=5, pady=5)

        self.entry_creditos_asignatura = ctk.CTkEntry(frame_metodos, placeholder_text="Créditos")
        self.entry_creditos_asignatura.pack(padx=5, pady=5)

        boton_agregar = ctk.CTkButton(frame_metodos, text="Añadir Asignatura", command=self.agregar_asignatura)
        boton_agregar.pack(padx=5, pady=5)

        boton_eliminar = ctk.CTkButton(frame_metodos, text="Eliminar Asignatura", command=self.eliminar_asignatura)
        boton_eliminar.pack(padx=5, pady=5)

        boton_modificar = ctk.CTkButton(frame_metodos, text="Modificar Asignatura", command=self.modificar_asignatura)
        boton_modificar.pack(padx=5, pady=5)

    def agregar_asignatura(self):
        nombre = self.entry_nombre_asignatura.get().strip()
        codigo = self.entry_codigo_asignatura.get().strip()
        creditos = self.entry_creditos_asignatura.get().strip()

        if not nombre or not codigo or not creditos:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        elif not creditos.isdigit() or int(creditos) <= 0:
            messagebox.showerror("Error", "Los créditos deben ser un número positivo")
        else:
            self.treeview_asignatura.insert("", "end", values=(nombre, codigo, creditos))

    def eliminar_asignatura(self):
        selected_item = self.treeview_asignatura.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione una asignatura para eliminar.")
            return
        self.treeview_asignatura.delete(selected_item)

    def modificar_asignatura(self):
        selected_item = self.treeview_asignatura.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione una asignatura para modificar.")
            return

        values = self.treeview_asignatura.item(selected_item)["values"]
        self.entry_nombre_asignatura.insert(0, values[0])
        self.entry_codigo_asignatura.insert(0, values[1])
        self.entry_creditos_asignatura.insert(0, values[2])

        # Eliminar la asignatura seleccionada
        self.eliminar_asignatura()

    def crear_pestaña_grupo(self):
        pestaña = self.tabview.add("Grupo")

        frame_metodos = ctk.CTkFrame(pestaña)
        frame_metodos.pack(side="left", padx=10, pady=10, fill="y")

        frame_datos = ctk.CTkFrame(pestaña)
        frame_datos.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.treeview_grupo = ttk.Treeview(frame_datos, columns=("nombre", "asignatura", "profesor"), show="headings")
        self.treeview_grupo.pack(expand=True, fill="both")

        self.treeview_grupo.heading("nombre", text="Nombre")
        self.treeview_grupo.heading("asignatura", text="Asignatura")
        self.treeview_grupo.heading("profesor", text="Profesor")

        self.entry_nombre_grupo = ctk.CTkEntry(frame_metodos, placeholder_text="Nombre")
        self.entry_nombre_grupo.pack(padx=5, pady=5)

        self.entry_asignatura_grupo = ctk.CTkEntry(frame_metodos, placeholder_text="Asignatura")
        self.entry_asignatura_grupo.pack(padx=5, pady=5)

        self.entry_profesor_grupo = ctk.CTkEntry(frame_metodos, placeholder_text="Profesor")
        self.entry_profesor_grupo.pack(padx=5, pady=5)

        boton_agregar = ctk.CTkButton(frame_metodos, text="Añadir Grupo", command=self.agregar_grupo)
        boton_agregar.pack(padx=5, pady=5)

        boton_eliminar = ctk.CTkButton(frame_metodos, text="Eliminar Grupo", command=self.eliminar_grupo)
        boton_eliminar.pack(padx=5, pady=5)

        boton_modificar = ctk.CTkButton(frame_metodos, text="Modificar Grupo", command=self.modificar_grupo)
        boton_modificar.pack(padx=5, pady=5)

        self.boton_inscribir = ctk.CTkButton(frame_metodos, text="Inscribir Estudiante", command=self.inscribir_estudiante_en_grupo)
        self.boton_inscribir.pack(padx=5, pady=5)

    def agregar_grupo(self):
        nombre = self.entry_nombre_grupo.get().strip()
        asignatura = self.entry_asignatura_grupo.get().strip()
        profesor = self.entry_profesor_grupo.get().strip()

        if not nombre or not asignatura or not profesor:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            self.treeview_grupo.insert("", "end", values=(nombre, asignatura, profesor))

    def eliminar_grupo(self):
        selected_item = self.treeview_grupo.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un grupo para eliminar.")
            return
        self.treeview_grupo.delete(selected_item)

    def modificar_grupo(self):
        selected_item = self.treeview_grupo.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un grupo para modificar.")
            return

        values = self.treeview_grupo.item(selected_item)["values"]
        self.entry_nombre_grupo.insert(0, values[0])
        self.entry_asignatura_grupo.insert(0, values[1])
        self.entry_profesor_grupo.insert(0, values[2])

        # Eliminar el grupo seleccionado
        self.eliminar_grupo()

    def inscribir_estudiante_en_grupo(self):
        selected_grupo = self.treeview_grupo.selection()
        selected_estudiante = self.treeview_estudiante.selection()

        if not selected_grupo:
            messagebox.showerror("Error", "Seleccione un grupo para inscribir al estudiante.")
            return
        if not selected_estudiante:
            messagebox.showerror("Error", "Seleccione un estudiante para inscribir en el grupo.")
            return

        estudiante_values = self.treeview_estudiante.item(selected_estudiante)["values"]
        grupo_values = self.treeview_grupo.item(selected_grupo)["values"]

        estudiante_nombre = estudiante_values[0]
        grupo_nombre = grupo_values[0]

        if not hasattr(self, 'inscripciones'):
            self.inscripciones = {}

        if grupo_nombre not in self.inscripciones:
            self.inscripciones[grupo_nombre] = []

        if estudiante_nombre in self.inscripciones[grupo_nombre]:
            messagebox.showerror("Error", f"El estudiante {estudiante_nombre} ya está inscrito en el grupo {grupo_nombre}.")
        else:
            self.inscripciones[grupo_nombre].append(estudiante_nombre)
            messagebox.showinfo("Éxito", f"Estudiante {estudiante_nombre} inscrito en el grupo {grupo_nombre}.")

    def crear_pestaña_programa_academico(self):
        pestaña = self.tabview.add("Programa Académico")

        frame_metodos = ctk.CTkFrame(pestaña)
        frame_metodos.pack(side="left", padx=10, pady=10, fill="y")

        frame_datos = ctk.CTkFrame(pestaña)
        frame_datos.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.treeview_programa_academico = ttk.Treeview(frame_datos, columns=("nombre", "duracion", "carrera"), show="headings")
        self.treeview_programa_academico.pack(expand=True, fill="both")

        self.treeview_programa_academico.heading("nombre", text="Nombre")
        self.treeview_programa_academico.heading("duracion", text="Duración")
        self.treeview_programa_academico.heading("carrera", text="Carrera")

        self.entry_nombre_programa = ctk.CTkEntry(frame_metodos, placeholder_text="Nombre")
        self.entry_nombre_programa.pack(padx=5, pady=5)

        self.entry_duracion_programa = ctk.CTkEntry(frame_metodos, placeholder_text="Duración")
        self.entry_duracion_programa.pack(padx=5, pady=5)

        self.entry_carrera_programa = ctk.CTkEntry(frame_metodos, placeholder_text="Carrera")
        self.entry_carrera_programa.pack(padx=5, pady=5)

        boton_agregar = ctk.CTkButton(frame_metodos, text="Añadir Programa Académico", command=self.agregar_programa_academico)
        boton_agregar.pack(padx=5, pady=5)

        boton_eliminar = ctk.CTkButton(frame_metodos, text="Eliminar Programa Académico", command=self.eliminar_programa_academico)
        boton_eliminar.pack(padx=5, pady=5)

        boton_modificar = ctk.CTkButton(frame_metodos, text="Modificar Programa Académico", command=self.modificar_programa_academico)
        boton_modificar.pack(padx=5, pady=5)

    def agregar_programa_academico(self):
        nombre = self.entry_nombre_programa.get().strip()
        duracion = self.entry_duracion_programa.get().strip()
        carrera = self.entry_carrera_programa.get().strip()

        if not nombre or not duracion or not carrera:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            self.treeview_programa_academico.insert("", "end", values=(nombre, duracion, carrera))

    def eliminar_programa_academico(self):
        selected_item = self.treeview_programa_academico.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un programa académico para eliminar.")
            return
        self.treeview_programa_academico.delete(selected_item)

    def modificar_programa_academico(self):
        selected_item = self.treeview_programa_academico.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un programa académico para modificar.")
            return

        values = self.treeview_programa_academico.item(selected_item)["values"]
        self.entry_nombre_programa.insert(0, values[0])
        self.entry_duracion_programa.insert(0, values[1])
        self.entry_carrera_programa.insert(0, values[2])

        # Eliminar el programa académico seleccionado
        self.eliminar_programa_academico()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()