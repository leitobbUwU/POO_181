import tkinter as tk
from Logica12 import Login
from tkinter import messagebox

class InterfazLogin:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Login")

        # Crear widgets de la interfaz gráfica
        tk.Label(ventana, text="Correo").grid(row=0, column=0)
        self.entry_correo = tk.Entry(ventana)
        self.entry_correo.grid(row=0, column=1)

        tk.Label(ventana, text="Contraseña").grid(row=1, column=0)
        self.entry_contraseña = tk.Entry(ventana, show="*")
        self.entry_contraseña.grid(row=1, column=1)

        self.boton_ingresar = tk.Button(ventana, text="Ingresar", command=self.verificar_ingreso)
        self.boton_ingresar.grid(row=2, column=1)

    def verificar_ingreso(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()
        login = Login(correo, contraseña)
        if login.login():
            mensaje = "Bienvenido, " + correo + "!"
        else:
            mensaje = "Revise sus datos e intente de nuevo."

        # Mostrar un mensaje de bienvenida o error
        messagebox.showinfo("Resultado", mensaje)
        
# Crear una ventana de Tkinter
ventana = tk.Tk()

# Crear una instancia de la clase InterfazLogin
interfaz_login = InterfazLogin(ventana)

# Iniciar el ciclo principal de la ventana
ventana.mainloop()