import tkinter as tk
from pruebaLogica import *

def generate_password_button_clicked():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_special_chars = special_chars_var.get()
    password, strength = generate_password_and_check_strength(length, include_uppercase, include_special_chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    strength_entry.delete(0, tk.END)
    strength_entry.insert(0, strength)

# Crear ventana principal
root = tk.Tk()
root.title('Password Generator')

# Crear campos de entrada
length_label = tk.Label(root, text='Length:')
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root, width=5)
length_entry.grid(row=0, column=1)
length_entry.insert(0, '8')

# Crear casillas de verificación
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text='Include uppercase', variable=uppercase_var)
uppercase_check.grid(row=1, column=0)

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text='Include special characters', variable=special_chars_var)
special_chars_check.grid(row=2, column=0)

# Crear botones
generate_button = tk.Button(root, text='Generate', command=generate_password_button_clicked)
generate_button.grid(row=3, column=0)

# Crear campos de salida
password_label = tk.Label(root, text='Password:')
password_label.grid(row=4, column=0)
password_entry = tk.Entry(root, width=20)
password_entry.grid(row=4, column=1)

strength_label = tk.Label(root, text='Strength:')
strength_label.grid(row=5, column=0)
strength_entry = tk.Entry(root, width=20)
strength_entry.grid(row=5, column=1)

# Ejecutar ventana principal
root.mainloop()