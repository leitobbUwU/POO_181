from tkinter import Tk, Button, messagebox, Entry, Label, Text
from tkinter import scrolledtext as st

#1.Instanciamos un objeto ventana
ventana= Tk()
ventana.title("Practica 11:3 Frames")
ventana.geometry("800x600")

titulo1 = Label(ventana, text="Usuario:")
titulo1.pack()
usuario = Entry(ventana)
usuario.pack()

titulo2 = Label(ventana, text="Contraseña:")
titulo2.pack()
contraseña = Entry(ventana, show="*")
contraseña.pack()

botonLog= Button(ventana, text="Boton Azul", fg="red", bg="#00ccff", font=("Helvetica", 15))
botonLog.pack()

ventana.mainloop()