import tkinter as tk
from tkinter import messagebox


class Window:
    def _init_(self, cosa):
        self.window=cosa
        self.window.title("Practica 11.3 Frames")
        self.window.geometry("800x600")
            
        self.longitud = tk.Entry(ventana, font=("Helvetica", 30), bg='#A9F5BC')
        self.longitud.pack(padx=20,pady=10)
        
        self.Generar= tk.Button(cosa, text="Boton Azul", fg="red", bg="#00ccff", font=("Helvetica", 15))
        self.Generar.pack()
        
        
ventana= tk.Tk()
Mostrar=Window(ventana)
ventana.mainloop()