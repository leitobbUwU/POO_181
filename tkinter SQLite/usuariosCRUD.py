import threading
from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import * 
#1. Mandamos a llamar los metodos dentro de la clase ControladorBD

#2. Creamos 1 objeto de la Clase ControladorBD
# ademas nos ayudara a iniciar los metodos de la clase
controlador= ControladorBD()

def ejecutaInsert():
    controlador.guardarUsuarios(varNom.get(), varCor.get(),varCon.get())
    
#4. Consultar registro de usuarios
def ejecutaSelectU():
    usuario=controlador.consultarUsuario(varBus.get())
    for usu in usuario:
        cadena= str(usu[0]) + " " + usu[1] + " " + usu[2] + " " + str(usu[3])
        
    if(usuario):
        #print(cadena)
        textEnc.insert(tk.END, cadena)
    else:
        messagebox.showinfo("No encontrado", "Ese usuario no existe en la BD")
        
def consultoria():
    return controlador.consultando()

def actualizar():
    # Borrar los registros actuales en la tabla
    for record in tree.get_children():
        tree.delete(record)

    # Obtener los nuevos registros de la base de datos
    datos = consultoria()

    # Agregar los nuevos registros a la tabla
    for i, row in enumerate(datos):
        tree.insert('', 'end', text=str(i+1), values=row)
        
def actualizar_tabla():
    t = threading.Thread(target=actualizar)
    t.start()
    

ventana=Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("800x600")

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='Yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

#Pestaña 1 registro de usuarios
titulo1 = Label(pestana1, text="Registro de usuarios", font=("Modern",20)).pack(fill=tk.X, padx=20,pady=5)

varNom=tk.StringVar()
titulo1 = Label(pestana1, text="Nombre:", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
usuario = Entry(pestana1, textvariable=varNom, font=("Helvetica", 18)).pack( padx=20,pady=10)
        
varCor = tk.StringVar()        
titulo2 = Label(pestana1, text="Correo:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
correo = Entry(pestana1,textvariable=varCor, font=("Helvetica", 18)).pack( padx=20, pady=10, )

varCon = tk.StringVar()
titulo3 = Label(pestana1, text="Contraseña:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
contraseña = Entry(pestana1, textvariable=varCon, show="*", font=("Helvetica", 18)).pack(padx=20, pady=10,)

botonLog= tk.Button(pestana1, text="Guardar Usuario", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutaInsert)
botonLog.pack()

#Inicio de la pestaña numero 2
titulo1 = Label(pestana2, text="Buscar de usuarios", font=("Modern",20)).pack(fill=tk.X, padx=20,pady=5)

varBus=tk.StringVar()
iblid = Label(pestana2, text="Identificador Usuario: ", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
txtid = Entry(pestana2, textvariable=varBus, font=("Helvetica", 18)).pack( padx=20,pady=10)
botonBus= tk.Button(pestana2, text="Buscar", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutaSelectU).pack()

iblid = Label(pestana2, text="Encontrado ",fg='blue', font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
textEnc=tk.Text(pestana2, height = 5, width=52)
textEnc.pack()

#Inicio de la tercer pestaña
columns = ('Usuario', 'Correo', 'Contraseña')
tree = ttk.Treeview(pestana3, columns=columns, show='headings')

tree.heading('Usuario', text='UsuarioDB')
tree.heading('Correo', text='CorreoDB')
tree.heading('Contraseña', text='ContraseñaDB')

tree.pack(padx=20, pady=10,)

# Obtención de los datos de la función consultoria() y agregación a Treeview
datos=consultoria()
for i, row in enumerate(datos):
    # Insertar datos de cada fila en el Treeview
    tree.insert('', 'end', text=str(i+1), values=row)

botonAct= tk.Button(pestana3, text="Actualizar", fg="Black", bg="#00ccff", font=("Modern", 15), command=actualizar_tabla).pack()

panel.add(pestana1, text='Formulario usuarios')
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuarios')
ventana.mainloop()
