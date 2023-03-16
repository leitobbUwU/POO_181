import tkinter as tk
from Variable import *
from tkinter import messagebox

def TomarDatos():
    letras = int(Año.get())
    contraseña = aleatorio(letras)
    messagebox.showinfo(text=contraseña)

window=tk.Tk()
window.title("Practica 14 Cajero Automatico")
window.geometry("800x600")        
titulo = tk.Label(window, text="Nombre:", font=("Helvetica", 15))
titulo.pack(fill=tk.X, padx=20, pady=5)
            
Nombre = tk.Entry(window, font=("Helvetica", 15), bg='#00ccff')
Nombre.pack(padx=20,pady=10)
        
titulo2 = tk.Label(window, text="Apellidos:", font=("Helvetica", 15))
titulo2.pack(fill=tk.X, padx=20, pady=5)
        
Apellidos = tk.Entry(window, font=("Helvetica", 15), bg='#00ccff')
Apellidos.pack(padx=20,pady=10)
        
titulo2 = tk.Label(window, text="Año de nacimiento:", font=("Helvetica", 15))
titulo2.pack(fill=tk.X, padx=20, pady=5)
        
Año = tk.Entry(window, font=("Helvetica", 15), bg='#00ccff')
Año.pack(padx=20,pady=10)
        
titulo2 = tk.Label(window, text="año de curso:", font=("Helvetica", 15))
titulo2.pack(fill=tk.X, padx=20, pady=5)
        
Curso = tk.Entry(window, font=("Helvetica", 15), bg='#00ccff')
Curso.pack(padx=20,pady=10)
        
titulo2 = tk.Label(window, text="Carrera:", font=("Helvetica", 15))
titulo2.pack(fill=tk.X, padx=20, pady=5)
        
Carrera = tk.Entry(window, font=("Helvetica", 15), bg='#00ccff')
Carrera.pack(padx=20,pady=10)
        
Generar= tk.Button(window, text="Generar contraseña", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=TomarDatos)
Generar.pack(padx=20,pady=10)
 
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

window.mainloop()