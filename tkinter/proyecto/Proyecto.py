import tkinter as tk
from logicaProyecto import Login
from logicaProyecto import Menu
from tkinter import messagebox

class Interfaz:
    def verificar(self):
        Usuario = self.usuario.get()
        Password = self.contraseña.get()
        login = Login(Usuario, Password)
        if login.login():
            mensaje="Bienvenido"
            self.ventana.destroy()
            Menu()
        else:
            mensaje = "Revise sus datos e intente de nuevo."
            if login.login() == None:
                mensaje = "un dato esta vacio"

        # Mostrar un mensaje de bienvenida o error
        messagebox.showinfo("Resultado", mensaje)
    
    def __init__(self, ventana):
#1.Instanciamos un objeto ventana
        self.ventana=ventana
        self.ventana.title("Practica 11.3 Frames")
        self.ventana.geometry("600x400")
        self.ventana.config(bg='#A9F5BC')

        titulo1 = tk.Label(ventana, text="Usuario:", font=("Helvetica",30), bg='#A9F5BC')
        titulo1.pack(padx=20,pady=5)
        self.usuario = tk.Entry(ventana, font=("Helvetica", 30), bg='#A9F5BC')
        self.usuario.pack(padx=20,pady=10)

        titulo2 = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 30), bg='#A9F5BC')
        titulo2.pack(padx=20, pady=5)
        self.contraseña = tk.Entry(ventana, show="*", font=("Helvetica", 30), bg='#A9F5BC')
        self.contraseña.pack(padx=20, pady=10, )

        self.Generar= tk.Button(ventana, text="Ingresar", fg="red", bg='#A9F5BC', font=("Helvetica", 15), command=self.verificar)
        self.Generar.pack()
        
        
    def CerrarVentana(self):
        ventana.destroy()
        

ventana= tk.Tk()
interfaz_login=Interfaz(ventana)
ventana.mainloop()