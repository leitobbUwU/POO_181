import tkinter as tk
from tkinter import Label, Entry, messagebox

class Tiendita:
    def __init__(self):
        self.productos = {
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
        self.total = 0
        self.carrito = []
        
        self.root = tk.Tk()
        self.root.title("Bienvenido a la tiendita")
        self.root.geometry("800x500")

        # Creamos un cuadro de lista para mostrar los productos
        self.listbox = tk.Listbox(self.root)
        for producto in self.productos:
            self.listbox.insert(tk.END, producto)
        self.listbox.pack()

        # Creamos un botón para agregar productos al carrito
        agregar_button = tk.Button(self.root, text="Agregar al carrito", command=self.agregar_producto)
        agregar_button.pack()

        # Creamos un botón para eliminar productos al carrito
        eliminar_button = tk.Button(self.root, text="Eliminar producto del carrito", command=self.eliminar_producto)
        eliminar_button.pack()

        # Creamos una etiqueta para mostrar el total a pagar
        self.total_label = tk.Label(self.root, text="Total: $0")
        self.total_label.pack()

        # Creamos un botón para finalizar compra
        comprar_button = tk.Button(self.root, text="Comprar", command=self.comprar_producto)
        comprar_button.pack()

        self.label = Label(self.root, text="Agregue su ubicación de favor:",fg="black")
        self.label.pack()
        self.ubicacion = Entry(self.root)
        self.ubicacion.pack()

        # Ejecutamos el bucle principal de la ventana
        self.root.mainloop()

    # Función para agregar un producto al carrito
    def agregar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        self.carrito.append(producto)
        precio = self.productos[producto]
        self.total += precio
        self.actualizar_total()

    # Función para eliminar un producto al carrito
    def eliminar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        self.carrito.remove(producto)
        precio = self.productos[producto]
        self.total -= precio
        self.actualizar_total()

    # Función para comprar productos del carrito
    def comprar_producto(self):
        if len(self.carrito) == 0:
            messagebox.showinfo("Error", "El carrito esta vacio.")
        else:
            messagebox.showinfo("Compra exitosa", "Su compra ha sido procesada.\nTotal a pagar: $" + str(self.total) + "\nCarrito de compras: " + "\n".join(self.carrito))
            self.carrito.clear()
            self.total = 0
            self.actualizar_total()

    # Función para actualizar el total a pagar
    def actualizar_total(self):
        self.total_label.config(text="Total: $" + str(self.total))
