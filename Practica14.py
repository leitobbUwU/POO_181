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
        
        self.Generar= tk.Button(cosa, text="Guardar datos", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.RealizarReg)
        self.Generar.pack()
        
        self.Generar= tk.Button(cosa, text="Consultar", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.MostrarRegistro)
        self.Generar.pack()
        
    def registroTitular(self):
        User = self.Titular.get()
        Registrar=datos(User) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "Registro de usuario exitoso " + User)
        else:
            messagebox.showerror("Error", "El usuario esta vacio.")
            
    def registroCuenta(self):
        Count= self.NoCuenta.get()
        Registrar=datos(Count)
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "La cuenta " + Count +" se registro exitosamente")
        else:
            messagebox.showerror("Error", "La cuenta esta vacia.")
            
    def registroEdad(self):
        Age= self.Edad.get()
        Registrar=datos(Age) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "Edad del titular: " + Age)
        else:
            messagebox.showerror("Error", "La edad está Vacia")
            
    def registroSaldo(self):
        Balance= self.Saldo.get()
        Registrar=datos(Balance) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "El saldo es de: " + Balance)
        else:
            messagebox.showerror("Error", "El campo saldo está vacío")
            
    def RealizarReg(self):
        self.registroTitular()
        self.registroCuenta()
        self.registroEdad()
        self.registroSaldo()
            
    def MostrarUsu(self):
        RegistroUsu=self.Titular.get()
        consultaUsu=datos(RegistroUsu)
        if consultaUsu.Guardar():
            messagebox.showinfo("Registro", "El usuario es: " + RegistroUsu) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en usuario.")
            
    def MostrarCoun(self):
        RegistroCoun=self.NoCuenta.get()
        consultaCoun=datos(RegistroCoun)
        if consultaCoun.Guardar():
            messagebox.showinfo("Registro", "La cuenta es: " + RegistroCoun) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en cuenta.")
            
    def MostrarEdad(self):
        RegistroEdad=self.Edad.get()
        consultaEdad=datos(RegistroEdad)
        if consultaEdad.Guardar():
            messagebox.showinfo("Registro", "La edad es: " + RegistroEdad) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en edad.")
            
    def MostrarSaldo(self):
        RegistroSaldo=self.Saldo.get()
        consultaSaldo=datos(RegistroSaldo)
        if consultaSaldo.Guardar():
            messagebox.showinfo("Registro", "El saldo es: " + RegistroSaldo) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en saldo.")
            
    def MostrarRegistro(self):
        self.MostrarUsu()
        self.MostrarCoun()
        self.MostrarEdad()
        self.MostrarSaldo()
        
ventana= tk.Tk()
Mostrar=Window(ventana)
ventana.mainloop()