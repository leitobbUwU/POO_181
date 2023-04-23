import sqlite3
from tkinter import *
from tkinter import messagebox

class Banco:
    def __init__(self):
        pass
    
    #Verificar la conexion a la base de datos
    def ConexionBd(self):
        try:
            conexion=sqlite3.connect("D:/documentos/GitHub/POO_181/Examen3P/BD_Banco.db")
            print("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("Error de conexión a la BD")
            
    #Metodo para mandar a registrar los datos de la interfaz
    def GuardarCuenSal(self, saldo, NoCuenta):
        coneccion=self.ConexionBd()
        #verificar que el entry no este vacio
        if(saldo == "" or NoCuenta == ""):
            messagebox.showwarning("Cuidado", "Formulario Vacio")
        else:
            #Preparamos el curosr
            cursor=coneccion.cursor() # type: ignore
            #Se crea la variable que guardara los datos
            info=(saldo, NoCuenta)
            Query="insert into TBCuentas(NoCuenta, Saldo) values(?,?)"
            
            #Se insertan los datos
            cursor.execute(Query,info)
            coneccion.commit() # type: ignore
            coneccion.close() # type: ignore
            messagebox.showinfo("Exito","Datos registrados")
            
    #Consultamos los datos registrados dentro de TBCuentas
    def ConsultaB(self):
        #Consultamos la conexion a la BD
        conectar=self.ConexionBd()
        
        cursor=conectar.cursor() # type: ignore
        try:
            select="select IDCuenta, NoCuenta, Saldo from TBCuentas"
            
            #Ejecutar y guardar la consulta
            cursor.execute(select)
            consulta=cursor.fetchall()
            conectar.close() # type: ignore
            
            #tomamos los datos guardados en la consulta y
            #los agregamos como una lista
            lista=[]
            for row in consulta:
                lista.append(list(row))
                
            #Regresamos la lista
            return lista
        except sqlite3.OperationalError:
            print("Error de consulta a la BD")
            
    def consultarID(self, NoC):
        conectar=self.ConexionBd()
        
        #Verificar si id contiene algo
        if(NoC==""):
            messagebox.showerror("Error", "El Numero de cuenta esta vacio")
            conectar.close() # type: ignore
            
        else:
            try:
                curso=conectar.cursor() # type: ignore
                select="select * from TBCuentas where NoCuenta="+NoC
                
                curso.execute(select)
                info=curso.fetchall()
                conectar.close() # type: ignore
                
                return info
            except sqlite3.OperationalError:
                print("Error de consulta")