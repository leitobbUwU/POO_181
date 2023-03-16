import tkinter as tk
from Variable import datos
from tkinter import messagebox

class Window:

    def __init__(self, cosa):
        self.window=cosa
        self.window.title("Practica 14 Cajero Automatico")
        self.window.geometry("1900x1000")

        
        titulo = tk.Label(cosa, text="Nombre:", font=("Helvetica", 15))
        titulo.pack(fill=tk.X, padx=20, pady=5)
            
        self.Nombre = tk.Entry(cosa, font=("Helvetica", 15), bg='#00ccff')
        self.Nombre.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(cosa, text="Apellidos:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Apellidos = tk.Entry(cosa, font=("Helvetica", 15), bg='#00ccff')
        self.Apellidos.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(cosa, text="Año de nacimiento:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Año = tk.Entry(cosa, font=("Helvetica", 15), bg='#00ccff')
        self.Año.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(cosa, text="año de curso:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Curso = tk.Entry(cosa, font=("Helvetica", 15), bg='#00ccff')
        self.Curso.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(cosa, text="Carrera:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Carrera = tk.Entry(cosa, font=("Helvetica", 15), bg='#00ccff')
        self.Carrera.pack(padx=20,pady=10)
        
        self.Generar= tk.Button(cosa, text="Generar contraseña", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.deposito2)
        self.Generar.pack(padx=20,pady=10)
        
        self.password = tk.Label(cosa, text="", font=("Helvetica", 15))
        self.password.pack(fill=tk.X, padx=20, pady=5)
 
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
    def deposito2(self):
        Name = self.Nombre.get()
        Name2 =self.Apellidos.get()
        Year = self.Año.get()
        Course = self.Curso.get()
        Program = self.Carrera.get()
        
        try:
            incluir2=float(self.Año.get())
            poner2 =float(self.Curso.get())
            if incluir2 != poner2:
                self.password.config(text=f"deposito exitoso: se se deposito {poner2:2f} en la cuenta Titular2.")
            else:
                self.password.config(text=f"Deposito exitoso: se transfirieron {poner2:2f} en la cuenta Titular2.")
        except:
            self.password.config(text="Error: todos los campos deben ser números.")        
    
    def registroCuenta(self):
        Count= self.Apellidos.get()
        Registrar=datos(Count)
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "La cuenta " + Count +" se registro exitosamente")
        else:
            messagebox.showerror("Error", "La cuenta esta vacia.")
            
    def registroEdad(self):
        Age= self.Curso.get()
        Registrar=datos(Age)
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "Edad del titular: " + Age)
        else:
            messagebox.showerror("Error", "La edad está Vacia")
            
    def registroSaldo(self):
        Balance= self.Carrera.get()
        RegistrarBalance=datos(Balance) # type: ignore
        if RegistrarBalance.Guardar():
            messagebox.showinfo("Exito", "El saldo es de: " + Balance)
        else:
            messagebox.showerror("Error", "El campo saldo está vacío")
            
    def RealizarReg(self):
        self.registroCuenta()
        self.registroEdad()
        self.registroSaldo()


ventana= tk.Tk()
Mostrar=Window(ventana)
ventana.mainloop()