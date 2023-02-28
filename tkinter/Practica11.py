
from tkinter import Tk, Frame, Button

#1.Instanciamos un objeto ventana
ventana= Tk()
ventana.title("Practica 11:3 Frames")
ventana.geometry("1200x800")

#2. Definimos las secciones de la ventana
seccion1=Frame(ventana, bg='#ff0000')
seccion1.pack(expand=True, fill='both')
seccion2=Frame(ventana, bg='#0000cc')
seccion2.pack(expand=True, fill='both')
seccion3=Frame(ventana, bg='#00ff00')
seccion3.pack(expand=True, fill='both')

#3. Botones
botonAzul= Button(seccion1, text="Botoan Azul", fg="red", bg="#00ccff")
botonAzul.place(x=60, y=60)

botonAmarillo= Button(seccion2, text="Boton Amarillo", fg="yellow", bg="black")
botonAmarillo.grid(row=0, column=0)
#botonAmarillo.place(x=60, y=60)

botonNegro= Button(seccion2, text="Boton Negro", fg="black", bg="white")
botonNegro.grid(row=1, column=1)
# botonNegro.place(x=60, y=60)

botonVerde= Button(seccion3, text="Boton Verde", fg="green", bg="white")
botonVerde.pack()
# botonNegro.place(x=60, y=60)

#Main de ejecucion de la ventana, tambien 
#tiene que ser la ultima linea de codigo, por ser el main.
ventana.mainloop()