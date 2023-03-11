import tkinter as tk
from Logica14 import datos
from tkinter import messagebox

class Window:

    def __init__(self, cosa):
        self.window=cosa
        self.window.title("Practica 11.3 Frames")
        self.window.geometry("800x600")
        
        titulo = tk.Label(ventana, text="Titular:", font=("Helvetica", 30))
        titulo.pack(fill=tk.X, padx=20, pady=5)
            
        self.Titular = tk.Entry(ventana, font=("Helvetica", 30), bg='#00ccff')
        self.Titular.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(ventana, text="NoCuenta:", font=("Helvetica", 30))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.NoCuenta = tk.Entry(ventana, font=("Helvetica", 30), bg='#00ccff')
        self.NoCuenta.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(ventana, text="Edad:", font=("Helvetica", 30))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Edad = tk.Entry(ventana, font=("Helvetica", 30), bg='#00ccff')
        self.Edad.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(ventana, text="Saldo:", font=("Helvetica", 30))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Saldo = tk.Entry(ventana, font=("Helvetica", 30), bg='#00ccff')
        self.Saldo.pack(padx=20,pady=10)
        
        self.Generar= tk.Button(cosa, text="Guardar datos", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.registro)
        self.Generar.pack()
        
        self.Generar= tk.Button(cosa, text="Consultar", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.MostrarReg)
        self.Generar.pack()
        
    def registro(self):
        User = self.Titular.get()
        Count= self.NoCuenta.get()
        Age= self.Edad.get()
        Balance= self.Saldo.get()
        
        Registrar=datos(User, Count, Age, Balance) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "Registro de usuario exitoso " + User)
        else:
            messagebox.showerror("El usuario esta vacio")
            
    def MostrarReg(self):
        Registro=self.Titular.get(), self.NoCuenta.get(), self.Edad.get(), self.Saldo.get()
        
        consulta=datos(Registro)
        if consulta.Guardar():
            messagebox.showinfo("Registro", "El registro es: " + Registro) # type: ignore
        else:
            messagebox.showerror("No hay datos")
        
ventana= tk.Tk()
Mostrar=Window(ventana)
ventana.mainloop()