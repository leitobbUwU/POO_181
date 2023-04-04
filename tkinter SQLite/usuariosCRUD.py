import threading
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
    #Limpiar la tabla
    pestana.delete(*pestana.get_children())
    usuario=controlador.consultarUsuario(varBus.get())
        
    if(usuario):
        #print(cadena)
        #textEnc.insert(tk.END, cadena)
        #self.heading.configure(text=cadena)
        for usu in usuario:
            pestana.insert('', 'end', values=(usu[0], usu[1], usu[2], usu[3]))
    else:
        messagebox.showinfo("No encontrado", "Ese usuario no existe en la BD")

#Importamos la lista de la BD
def consultoria():
    return controlador.consultando()

#Actualizamos la parte grafica mandando a borrar y mostrar la nueva BD
def actualizar():
    # Borrar los registros actuales en la tabla
    for record in tree.get_children():
        tree.delete(record)

    # Obtener los nuevos registros de la base de datos
    datos = consultoria()

    # Agregar los nuevos registros a la tabla
    for i, row in enumerate(datos): # type: ignore
        tree.insert('', 'end', text=str(i+1), values=row)

#Creamos una funcion para que la tabla se actualice al dar clic en el boton 
def actualizar_tabla():
    t = threading.Thread(target=actualizar)
    t.start()
    
def Renombrar():
    controlador.actualizarUsuario(txtidRe.get(), NomRen.get(), CorRen.get(),ConRen.get()) # type: ignore

def eliminar():
    controlador.eliminarUsuario(txtidRe.get())

ventana=Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("800x600")

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand=True)

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

columnas = ('Id', 'Usuario', 'Correo', 'Contraseña')
pestana = ttk.Treeview(pestana2, columns=columnas, show='headings')

pestana.heading('Id', text='IdDB')
pestana.heading('Usuario', text='UsuarioDB')
pestana.heading('Correo', text='CorreoDB')
pestana.heading('Contraseña', text='ContraseñaDB')

pestana.pack(padx=20, pady=10,)

#Inicio de la tercer pestaña
columns = ('Id', 'Usuario', 'Correo', 'Contraseña')
tree = ttk.Treeview(pestana3, columns=columns, show='headings')

tree.heading('Id', text='IdDB')
tree.heading('Usuario', text='UsuarioDB')
tree.heading('Correo', text='CorreoDB')
tree.heading('Contraseña', text='ContraseñaDB')

tree.pack(padx=20, pady=10,)

# Obtención de los datos de la función consultoria() y agregación a Treeview
datos=consultoria()
for i, row in enumerate(datos): # type: ignore
    # Insertar datos de cada fila en el Treeview
    tree.insert('', 'end', text=str(i+1), values=row)

botonAct= tk.Button(pestana3, text="Actualizar", fg="Black", bg="#00ccff", font=("Modern", 15), command=actualizar_tabla).pack()

#Inicio de la cuarta pestana
iblid = Label(pestana4, text="Ingrese un ID valido por favor: ", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
txtidRe = Entry(pestana4, textvariable=varBus, font=("Helvetica", 18))
txtidRe.pack( padx=20,pady=10)

titulo1 = Label(pestana4, text="Renombrar ", font=("Modern",20)).pack(fill=tk.X, padx=20,pady=5)

NomRen=tk.StringVar()
titulo1 = Label(pestana4, text="Nombre:", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
usuarioRe = Entry(pestana4, textvariable=NomRen, font=("Helvetica", 18))
usuarioRe.pack( padx=20,pady=10)
        
CorRen = tk.StringVar()        
titulo2 = Label(pestana4, text="Correo:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
correoRe = Entry(pestana4,textvariable=CorRen, font=("Helvetica", 18))
correoRe.pack( padx=20, pady=10, )

ConRen = tk.StringVar()
titulo3 = Label(pestana4, text="Contraseña:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
contraseñaRe = Entry(pestana4, textvariable=ConRen, show="*", font=("Helvetica", 18))
contraseñaRe.pack(padx=20, pady=10,)

botonRen= tk.Button(pestana4, text="Guardar Nuevo Usuario", fg="Black", bg="#00ccff", font=("Modern", 15), command=Renombrar)
botonRen.pack()

botonBorrar= tk.Button(pestana4, text="Borrar ID", fg="Black", bg="#00ccff", font=("Modern", 15), command=eliminar)
botonBorrar.pack()

panel.add(pestana1, text='Formulario usuarios')
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar registro y Borrar registro')

ventana.mainloop()
