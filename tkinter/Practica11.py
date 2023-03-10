
from tkinter import Tk, Frame, Button, messagebox

#4. Crear función para mandar a mostrar mensaje desde botón azul
def mostrarMensaje():
    messagebox.showinfo("Warning","Que onda pa")
    messagebox.showerror("Error", "Todo fallo con exito")
    print(messagebox.askokcancel("Pregunta seria", "¿El o ella jugo con tu corazón?"))
    print(messagebox.askquestion("Pregunta","¿Esto es una pregunta?"))
    print(messagebox.askretrycancel("Pregunta","¿Esto es una pregunta?"))
    print(messagebox.askyesno("Pregunta","¿Esto es una pregunta?"))
    print(messagebox.askyesnocancel("Pregunta","¿Esto es una pregunta?"))
    
#5. Funcion para agregar botones
def agregarBoton():
    botonVerde.config(text="+", bg="black", fg="white")
    botonNuevo= Button(seccion3, text="Boton nuevo", font=("Helvetica", 20))
    botonNuevo.pack()

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
botonAzul= Button(seccion1, text="Boton Azul", fg="red", bg="#00ccff", font=("Helvetica", 20),command=mostrarMensaje)
botonAzul.place(x=60, y=60)

botonAmarillo= Button(seccion2, text="Boton Amarillo", fg="yellow", bg="black", font=("Helvetica", 20))
botonAmarillo.grid(row=0, column=0)
#botonAmarillo.place(x=60, y=60)

botonNegro= Button(seccion2, text="Boton Negro", fg="black", bg="white", font=("Helvetica", 20))
botonNegro.grid(row=1, column=1)
# botonNegro.place(x=60, y=60)

botonVerde= Button(seccion3, text="Boton Verde", fg="green", bg="white", command= agregarBoton, font=("Helvetica", 20))
botonVerde.pack()
# botonNegro.place(x=60, y=60)

#Main de ejecucion de la ventana, tambien 
#tiene que ser la ultima linea de codigo, por ser el main.
ventana.mainloop()
