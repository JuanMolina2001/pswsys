from tkinter import Menu,Tk
from .importPsw import ImportPasswords


class BarMenu:
    def __init__(self, window: Tk):
        self.window = window
        self.menu_bar = Menu(window)
        # Archivo
        archivo_menu = Menu(self.menu_bar, tearoff=0)
        archivo_menu.add_command(label="Import passwords", command=lambda: ImportPasswords(self.window))
        archivo_menu.add_command(label="Salir", command=window.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        # Editar
        editar_menu = Menu(self.menu_bar, tearoff=0)
        editar_menu.add_command(label="Deshacer", command=self.deshacer)
        editar_menu.add_command(label="Rehacer", command=self.rehacer)
        self.menu_bar.add_cascade(label="Editar", menu=editar_menu)

        # Asignar la barra de menú a la ventana
        window.config(menu=self.menu_bar)

    def deshacer(self):
        print("Deshacer acción")

    def rehacer(self):
        print("Rehacer acción")
