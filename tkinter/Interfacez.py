import tkinter as tk
from tkinter import messagebox, Label, Button

ventana= tk.Tk()
ventana=ventana
ventana.title("Practica 11.3 Frames")
ventana.geometry("800x600")

titulo2 =Label(ventana, text="Contraseña:", font=("Helvetica", 30))
titulo2.pack(fill=tk.X, padx=20, pady=5)
ventana.mainloop()