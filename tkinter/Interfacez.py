import tkinter as tk
from tkinter import messagebox, Label, Button


def Interfaz1():
    ventana= tk.Tk()
    ventana=ventana
    ventana.title("Practica 11.3 Frames")
    ventana.geometry("800x600")

ventana= tk.Tk()
ventana=ventana
ventana.title("Practica 11.3 Frames")
ventana.geometry("800x600")

botonLog=Button(ventana, text="Boton Azul", fg="red", bg="#00ccff", font=("Helvetica", 15), command=Interfaz1)
botonLog.pack()

ventana.mainloop()