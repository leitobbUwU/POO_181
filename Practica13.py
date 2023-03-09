import tkinter as tk
from Logica13 import *
from tkinter import messagebox


class Window:
    def __init__(self, cosa):
        self.window=cosa
        self.window.title("Practica 11.3 Frames")
        self.window.geometry("800x600")
            
        self.longitud = tk.Entry(ventana, font=("Helvetica", 30), bg='#6FE74B')
        self.longitud.pack(padx=20,pady=10)
        
        self.Generar= tk.Button(cosa, text="Boton Azul", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command= self.Longitud)
        self.Generar.pack()
        
    def Longitud(self):
        Tamaño = self.longitud.get()
        Gen= password(self, Tamaño)
        # Verificar que la longitud es un entero positivo
        if Gen.crafteo():
            correcto = password.crafteo
            #messagebox.showinfo("Contraseña: "{correcto.get()})
        else:
            contrasena = password.crafteo
        
ventana= tk.Tk()
Mostrar=Window(ventana)
ventana.mainloop()