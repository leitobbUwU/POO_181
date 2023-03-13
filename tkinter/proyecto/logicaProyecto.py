import tkinter as tk
import tkinter as tk
from tkinter import Entry, Label, Tk, TkVersion

class Menu:
    
    print("")
    print("")
    print("")
    print("")
    print("")
    productos = {
            "Coca-cola 600ML $16": 16,
            "Sabritas $20": 20,
            "Garrafon de Agua $50": 50,
            "Pan Bimbo $45": 45,
            "Tortillas $22": 22,
            "Fabuloso $30": 30,
            "Cloro $20": 20,
            "Cepillo de dientes $17": 17,
            "Leche $26": 26,
            "Mazapan $7": 7
        }
    
    total = int(0)
    carrito = []
    
    # Función para eliminar un producto al carrito
    def comprar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        carrito.append(producto)
        precio = productos[producto]
        global total
        total += precio
        actualizar_total()

    # Función para eliminar un producto al carrito
    def eliminar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        carrito.append(producto)
        precio = productos[producto]
        global total
        total += precio
        actualizar_total()

    # Función para agregar un producto al carrito
    def agregar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        carrito.append(producto)
        precio = productos[producto]
        global total
        total += precio
        self.actualizar_total()

    # Función para actualizar el total a pagar
    def actualizar_total(self):
        self.total_label.config(text="Total: $" + str(total))
        
    # Creamos la ventana principal
    root = tk.Tk()
    root.title("Bienvenido a la tiendita")
    root.geometry("800x500")

    # Creamos un cuadro de lista para mostrar los productos
    listbox = tk.Listbox(root)
    for producto in productos:
        listbox.insert(tk.END, producto)
    listbox.pack()

    # Creamos un botón para agregar productos al carrito
    agregar_button = tk.Button(root, text="Agregar al carrito", command=agregar_producto)
    agregar_button.pack()

    # Creamos un botón para eliminar productos al carrito
    eliminar_button = tk.Button(root, text="Eliminar producto del carrito", command=eliminar_producto)
    eliminar_button.pack()

    # Creamos una etiqueta para mostrar el total a pagar
    total_label = tk.Label(root, text="Total: $0")
    total_label.pack()

    # Creamos un botón para finalizar compra
    comprar_button = tk.Button(root, text="Comprar", command=comprar_producto)
    comprar_button.pack()
    
class Login:
    def __init__(self, usuario, contraseña):
            self.usuario = usuario
            self.contraseña = contraseña

    def login(self):
        if self.usuario == "Usuario" and self.contraseña == "Admin":
            return True
        else:
            return False