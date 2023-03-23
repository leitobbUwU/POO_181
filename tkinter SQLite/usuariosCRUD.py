from tkinter import *
from tkinter import ttk
import tkinter as tk


ventana=Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("800x600")

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

varNom=tk.StringVar()
titulo1 = Label(pestana1, text="Nombre:", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
usuario = Entry(pestana1, textvariable=varNom, font=("Helvetica", 18)).pack(fill=tk.X, padx=20,pady=10)
        
varCor = tk.StringVar()        
titulo2 = Label(pestana1, text="Correo:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
correo = Entry(pestana1,textvariable=varCor, show="*", font=("Helvetica", 18)).pack(fill=tk.X, padx=20, pady=10, )

varCon = tk.StringVar()
titulo3 = Label(pestana1, text="Contraseña:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
contraseña = Entry(pestana1, textvariable=varCon, show="*", font=("Helvetica", 18)).pack(fill=tk.X, padx=20, pady=10, )

botonLog= tk.Button(pestana1, text="Guardar Usuario", fg="Black", bg="#00ccff", font=("Modern", 15))
botonLog.pack()

panel.add(pestana1, text='Formulario usuarios')
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuarios')

ventana.mainloop()

"""
class Interfaz:
    def __init__(self, ventana):
#1.Instanciamos un objeto ventana
        self.ventana=ventana
        self.ventana.title("CRUD de Usuarios")
        self.ventana.geometry("800x600")

        titulo1 = tk.Label(ventana, text="Nombre:", font=("Helvetica",30))
        titulo1.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = tk.Entry(ventana, font=("Helvetica", 30))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)
        
        titulo2 = tk.Label(ventana, text="Correo:", font=("Helvetica", 30))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        self.correo = tk.Entry(ventana, show="*", font=("Helvetica", 30))
        self.correo.pack(fill=tk.X, padx=20, pady=10, )

        titulo2 = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 30))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        self.contraseña = tk.Entry(ventana, show="*", font=("Helvetica", 30))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10, )

        self.botonLog= tk.Button(ventana, text="Guardar Usuario", fg="red", bg="#00ccff", font=("Helvetica", 15), command=self.verificar)
        self.botonLog.pack()
        
    def verificar(self):
        Usuario = self.usuario.get()
        Password = self.contraseña.get()
        login = Login(Usuario, Password)
        if login.login():
            mensaje = "Bienvenido, " + Usuario + "!"
        else:
            mensaje = "Revise sus datos e intente de nuevo."
            if login.login() == None:
                mensaje = "un dato esta vacio"

        # Mostrar un mensaje de bienvenida o error
        messagebox.showinfo("Resultado", mensaje)
            
        

ventana= tk.Tk()
interfaz_login=Interfaz(ventana)
ventana.mainloop()
"""