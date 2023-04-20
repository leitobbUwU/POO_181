import threading
from tkinter import ttk
import tkinter as tk
from controladorBD import *

controlador=Banco()

def Guardar():    
    cuenta= NoCuenta.get()
    saldo=Saldo.get()
    
    if cuenta.isdigit() or saldo.isdigit():
        controlador.GuardarCuenSal(NoCuenta.get(), Saldo.get())
        messagebox.showinfo("Exito", "El dato es un numero valido")        
    else:
        messagebox.showerror("Error", "El dato no es un numero")

def consultar():
    return controlador.ConsultaB()

def actualizar():
    for record in tree.get_children():
        tree.delete(record)
        
    datos=consultar()
    
    for i, row in enumerate(datos):
        tree.insert('', 'end', text=str(i+1), values=row)

def actualizarTab():
    o = threading.Thread(target=actualizar)
    o.start()   

ventana=Tk()
ventana.title("Examen Parcial tres")
ventana.geometry("800x900")
    
panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand=True)
    
pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)

NoCuenta=tk.StringVar()
titulo=Label(pestana1, text="NoCuenta").pack(fill=tk.X, padx=20, pady=5)
NoCuentaEn=Entry(pestana1, textvariable=NoCuenta).pack(padx=20,pady=10)

Saldo=tk.StringVar()
titulo=Label(pestana1, text="Saldo").pack(fill=tk.X, padx=20, pady=5)
SaldoEn=Entry(pestana1, textvariable=Saldo).pack(padx=20,pady=10)

BotonG=tk.Button(pestana1, text="Guardar Datos", command=Guardar)
BotonG.pack()

#Inicio la pestaña dos
columnas=('ID', 'Nocuenta', 'Saldo')
tree = ttk.Treeview(pestana2, columns=columnas, show='headings')

tree.heading('ID', text='Id')
tree.heading('Nocuenta', text='Nocuenta')
tree.heading('Saldo', text='Saldo')

tree.pack(padx=20, pady=10)


panel.add(pestana1, text="Ingrese datos")
panel.add(pestana2, text="Actualizar y consultar")

ventana.mainloop()