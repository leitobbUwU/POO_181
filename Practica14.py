import tkinter as tk
from Logica14 import datos
from tkinter import messagebox

class Window:

    def __init__(self, cosa):
        self.window=cosa
        self.window.title("Practica 14 Cajero Automatico")
        self.window.geometry("1900x1000")
        
        frame1=tk.Frame(ventana)
        frame2=tk.Frame(ventana)
        frame3=tk.Frame(ventana)
        frame1.pack(side="left", fill=tk.Y)
        frame2.pack(side="right", fill=tk.Y)
        frame3.pack(side="top")
        
        titulo = tk.Label(frame1, text="Titular:", font=("Helvetica", 15))
        titulo.pack(fill=tk.X, padx=20, pady=5)
            
        self.Titular = tk.Entry(frame1, font=("Helvetica", 15), bg='#00ccff')
        self.Titular.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(frame1, text="NoCuenta:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.NoCuenta = tk.Entry(frame1, font=("Helvetica", 15), bg='#00ccff')
        self.NoCuenta.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(frame1, text="Edad:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Edad = tk.Entry(frame1, font=("Helvetica", 15), bg='#00ccff')
        self.Edad.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(frame1, text="Saldo:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Saldo = tk.Entry(frame1, font=("Helvetica", 15), bg='#00ccff')
        self.Saldo.pack(padx=20,pady=10)
        
        self.Generar= tk.Button(frame1, text="Guardar datos", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.RealizarReg)
        self.Generar.pack(padx=20,pady=10)
        
        self.consultar= tk.Button(frame1, text="Consultar", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.MostrarRegistro)
        self.consultar.pack(padx=20,pady=10)
        
        #////////////////////////////////////////////////////////////////////////////////////////////////////////
       
        titulo = tk.Label(frame2, text="Titular 2:", font=("Helvetica", 15))
        titulo.pack(fill=tk.X, padx=20, pady=5)
            
        self.Titular2 = tk.Entry(frame2, font=("Helvetica", 15), bg='#00ccff')
        self.Titular2.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(frame2, text="Segundo NoCuenta:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.NoCuenta2 = tk.Entry(frame2, font=("Helvetica", 15), bg='#00ccff')
        self.NoCuenta2.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(frame2, text="Segunda Edad:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Edad2 = tk.Entry(frame2, font=("Helvetica", 15), bg='#00ccff')
        self.Edad2.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(frame2, text="Segundo Saldo:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.Saldo2 = tk.Entry(frame2, font=("Helvetica", 15), bg='#00ccff')
        self.Saldo2.pack(padx=20,pady=10)
        
        self.Generar2= tk.Button(frame2, text="Guardar datos secundarios", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.RealizarReg2)
        self.Generar2.pack(padx=20,pady=10)
        
        self.consultar2= tk.Button(frame2, text="Consultar datos secundarios", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.MostrarRegistro2)
        self.consultar2.pack(padx=20,pady=10)
        
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        titulo2 = tk.Label(frame3, text="transferencia:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.transaccion = tk.Entry(frame3, font=("Helvetica", 15), bg='#00ccff')
        self.transaccion.pack(padx=20,pady=10)
        
        self.Mandar= tk.Button( frame3, text="Transferir Titular2", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.transferir)
        self.Mandar.pack(padx=20,pady=10)
        
        self.Mandar2= tk.Button( frame3, text="Transferir Titular", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.transferir2)
        self.Mandar2.pack(padx=20,pady=10)
        
        self.respuesta = tk.Label(frame3, font=("Helvetica", 15))
        self.respuesta.pack(fill=tk.X, padx=20, pady=5)
        
         #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        titulo2 = tk.Label(frame3, text="Deposito:", font=("Helvetica", 15))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        
        self.dep = tk.Entry(frame3, font=("Helvetica", 15), bg='#00ccff')
        self.dep.pack(padx=20,pady=10)
        
        self.depositando1= tk.Button( frame3, text="Depositar Titular", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.deposito)
        self.depositando1.pack()
        
        self.Mandar= tk.Button( frame3, text="Depositar Titular2", fg="#000000", bg="#FFFFFF", font=("Roman", 15), command=self.deposito2)
        self.Mandar.pack(padx=20,pady=10)
        
        self.depositando = tk.Label(frame3, font=("Helvetica", 15))
        self.depositando.pack(fill=tk.X, padx=20, pady=5)
        
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
    def registroTitular(self):
        User = self.Titular.get()
        Registrar=datos(User) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "Registro de usuario exitoso " + User)
        else:
            messagebox.showerror("Error", "El usuario esta vacio.")
            
    def registroCuenta(self):
        Count= self.NoCuenta.get()
        Registrar=datos(Count) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "La cuenta " + Count +" se registro exitosamente")
        else:
            messagebox.showerror("Error", "La cuenta esta vacia.")
            
    def registroEdad(self):
        Age= self.Edad.get()
        Registrar=datos(Age) # type: ignore
        if Registrar.Guardar():
            messagebox.showinfo("Exito", "Edad del titular: " + Age)
        else:
            messagebox.showerror("Error", "La edad está Vacia")
            
    def registroSaldo(self):
        global Balance
        Balance= self.Saldo.get()
        RegistrarBalance=datos(Balance) # type: ignore
        if RegistrarBalance.Guardar():
            messagebox.showinfo("Exito", "El saldo es de: " + Balance)
        else:
            messagebox.showerror("Error", "El campo saldo está vacío")
        return Balance
            
    def RealizarReg(self):
        self.registroTitular()
        self.registroCuenta()
        self.registroEdad()
        self.registroSaldo()
            
    def MostrarUsu(self):
        RegistroUsu=self.Titular.get()
        consultaUsu=datos(RegistroUsu) # type: ignore
        if consultaUsu.Guardar():
            messagebox.showinfo("Registro", "El usuario es: " + RegistroUsu) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en usuario.")
            
    def MostrarCoun(self):
        RegistroCoun=self.NoCuenta.get()
        consultaCoun=datos(RegistroCoun) # type: ignore
        if consultaCoun.Guardar():
            messagebox.showinfo("Registro", "La cuenta es: " + RegistroCoun) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en cuenta.")
            
    def MostrarEdad(self):
        RegistroEdad=self.Edad.get()
        consultaEdad=datos(RegistroEdad) # type: ignore
        if consultaEdad.Guardar():
            messagebox.showinfo("Registro", "La edad es: " + RegistroEdad) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en edad.")
            
    def MostrarSaldo(self):
        RegistroSaldo=self.Saldo.get()
        consultaSaldo=datos(RegistroSaldo) # type: ignore
        if consultaSaldo.Guardar():
            messagebox.showinfo("Registro", "El saldo es: " + RegistroSaldo) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en saldo.")
            
    def MostrarRegistro(self):
        self.MostrarUsu()
        self.MostrarCoun()
        self.MostrarEdad()
        self.MostrarSaldo()
        
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
   
   #Creacion de las funciones para guardar los entry en una variable y luego poderlos leer
        
    def registroTitular2(self):
        User2 = self.Titular2.get()
        Registrar2=datos(User2) # type: ignore
        if Registrar2.Guardar():
            messagebox.showinfo("Exito", "Registro de usuario exitoso " + User2)
        else:
            messagebox.showerror("Error", "El usuario esta vacio.")
            
    def registroCuenta2(self):
        Count2= self.NoCuenta2.get()
        Registrar2=datos(Count2) # type: ignore
        if Registrar2.Guardar():
            messagebox.showinfo("Exito", "La cuenta " + Count2 +" se registro exitosamente")
        else:
            messagebox.showerror("Error", "La cuenta esta vacia.")
            
    def registroEdad2(self):
        Age2= self.Edad2.get()
        Registrar2=datos(Age2) # type: ignore
        if Registrar2.Guardar():
            messagebox.showinfo("Exito", "Edad del titular: " + Age2)
        else:
            messagebox.showerror("Error", "La edad está Vacia")
            
    def registroSaldo2(self):
        global Balance2
        Balance2= self.Saldo2.get()
        RegistrarBalance2=datos(Balance2) # type: ignore
        if RegistrarBalance2.Guardar():
            messagebox.showinfo("Exito", "El saldo es de: " + Balance2)
        else:
            messagebox.showerror("Error", "El campo saldo está vacío")
        return Balance2
    
    #Funcion que mandara a llamar las funciones anteriores y 
    #mostrara los messagebox de registro correspondiente a cada campo.
    
    def RealizarReg2(self):
        self.registroTitular2()
        self.registroCuenta2()
        self.registroEdad2()
        self.registroSaldo2()
        
    #Misma logica de arriba, pero esta 
        
    def MostrarUsu2(self):
        RegistroUsu2=self.Titular2.get()
        consultaUsu2=datos(RegistroUsu2) # type: ignore
        if consultaUsu2.Guardar():
            messagebox.showinfo("Registro", "El usuario es: " + RegistroUsu2) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en usuario.")
            
    def MostrarCoun2(self):
        RegistroCoun2=self.NoCuenta2.get()
        consultaCoun2=datos(RegistroCoun2) # type: ignore
        if consultaCoun2.Guardar():
            messagebox.showinfo("Registro", "La cuenta es: " + RegistroCoun2) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en cuenta.")
            
    def MostrarEdad2(self):
        RegistroEdad2=self.Edad2.get()
        consultaEdad2=datos(RegistroEdad2) # type: ignore
        if consultaEdad2.Guardar():
            messagebox.showinfo("Registro", "La edad es: " + RegistroEdad2) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en edad.")
            
    def MostrarSaldo2(self):
        RegistroSaldo2=self.Saldo2.get()
        consultaSaldo2=datos(RegistroSaldo) # type: ignore
        if consultaSaldo2.Guardar():
            messagebox.showinfo("Registro", "El saldo es: " + RegistroSaldo2) # type: ignore
        else:
            messagebox.showerror("Error", "No hay registro en saldo.") 
        
    def MostrarRegistro2(self):
        self.MostrarUsu2()
        self.MostrarCoun2()
        self.MostrarEdad2()
        self.MostrarSaldo2()
    
    
    def transferir(self):
        try:
            cantidad1=float(self.Saldo.get())
            cantidad2=float(self.Saldo2.get())
            monto =float(self.transaccion.get())
            if cantidad1 >= monto:
                cantidad1 -= monto
                cantidad2 += monto
                self.Saldo.delete(0, tk.END)
                self.Saldo.insert(0, str(cantidad1))
                self.Saldo2.delete(0, tk.END)
                self.Saldo2.insert(0, str(cantidad2))
                self.respuesta.config(text=f"Transferencia exitosa: se transfirieron {monto:.2f} de la cuenta Titular a la cuenta Titular2.")
            else:
                self.respuesta.config(text=f"Transferencia exitosa: se transfirieron {monto:.2f} de la cuenta Titular a la cuenta Titular2.")
        except:
            self.respuesta.config(text="Error: todos los campos deben ser números.")
    
    
    def transferir2(self):
        try:
            canti1=float(self.Saldo.get())
            canti2=float(self.Saldo2.get())
            mon =float(self.transaccion.get())
            if canti1 >= mon:
                canti2 -= mon
                canti1 += mon
                self.Saldo.delete(0, tk.END)
                self.Saldo.insert(0, str(canti1))
                self.Saldo2.delete(0, tk.END)
                self.Saldo2.insert(0, str(canti2))
                self.respuesta.config(text=f"Transferencia exitosa: se transfirieron {mon:.2f} de la cuenta Titular2 a la cuenta Titular.")
            else:
                self.respuesta.config(text=f"Transferencia exitosa: se transfirieron {mon:.2f} de la cuenta Titular2 a la cuenta Titular.")
        except:
            self.respuesta.config(text="Error: todos los campos deben ser números.")
          
          
  
    def deposito(self):
        try:
            incluir=float(self.Saldo.get())
            poner =float(self.dep.get())
            if incluir >= poner:
                incluir += poner
                self.Saldo.delete(0, tk.END)
                self.Saldo.insert(0, str(incluir))
                self.depositando.config(text=f"deposito exitoso: se se deposito {poner:.2f} en la cuenta Titular.")
            else:
                 self.depositando.config(text=f"Deposito exitoso: se transfirieron {poner:.2f} en la cuenta Titular.")
        except:
            self.depositando.config(text="Error: todos los campos deben ser números.")
            

    def deposito2(self):
        try:
            incluir2=float(self.Saldo2.get())
            poner2 =float(self.dep.get())
            if incluir2 >= poner2:
                incluir2 += poner2
                self.Saldo2.delete(0, tk.END)
                self.Saldo2.insert(0, str(incluir2))
                self.depositando.config(text=f"deposito exitoso: se se deposito {poner2:.2f} en la cuenta Titular2.")
            else:
                self.depositando.config(text=f"Deposito exitoso: se transfirieron {poner2:.2f} en la cuenta Titular2.")
        except:
            self.depositando.config(text="Error: todos los campos deben ser números.")

ventana= tk.Tk()
Mostrar=Window(ventana)
ventana.mainloop()