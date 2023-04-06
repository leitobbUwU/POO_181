from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:
    
    def __init__(self):
        pass
    
    # Metodo para intentar una conexión a la BD
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/documentos/GitHub/POO_181/tkinter SQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion            
        except sqlite3.OperationalError:
            print("Error de conexion a la BD")
        
    # Metodo para capturar datos del entry
    def guardarUsuarios(self, nom, cor, con):
        
        #1. usamos una conexión para registrar
        conx= self.conexionBD()
        
        #2. Checar que el entry contenga algo
        if(nom== " " or cor == "" or con == ""):
            messagebox.showwarning("Aguas", "Formulario incompleto")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor() # type: ignore
            # Se manda a encriptar la contraseña y se agrega en el paquete de datos enviados a la BD
            conH= self.encriptarCon(con)
            datos=(nom, cor, conH)
            qrInsert= "insert into TBRegistrados(nombre, correo, contra) values(?,?,?)"
            
            #4. Ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert, datos)
            conx.commit() # type: ignore
            conx.close() # type: ignore
            messagebox.showinfo("Exito", "Usuario Guardado")
            
    # Metodo para encriptar la contraseña
    def encriptarCon(self, con):
        conPlana= con
        # Se convierte con a bytes
        conPlana= conPlana.encode()
        # Le hecha la sal a la contraseña
        sal= bcrypt.gensalt()
        
        # Encriptamos la contraseña
        conHa= bcrypt.hashpw(conPlana, sal)
        print(conHa)
        
        # Envia la contraseña
        return conHa
    
    #Metodo para consulta de usuario
    def consultarUsuario(self,id):
        #1. Preparar una condición
        conx= self.conexionBD()
        
        #2. Verificar si id contiene algo
        if(id==""):
            messagebox.showerror("Error", "ID vacio, escribe un usuario valido.")
            conx.close() # type: ignore
        else:
            try:
                #3. Preparar el cursor y el qwery
                cursor=conx.cursor() # type: ignore
                selectQry= "select * from TBRegistrados where id="+id
                
                #4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario=cursor.fetchall()
                conx.close() # type: ignore
                
                return rsUsuario
                
            except sqlite3.OperationalError:
                print("Error consulta")
                
    def consultando(self):
        #1. Preparar una condición
        conx= self.conexionBD()
        #3. Preparar el cursor y el qwery
        cursor=conx.cursor() # type: ignore
        try:
            selectQry= "select id, nombre, correo, contra from TBRegistrados"
                    
            #4. ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsUsuario=cursor.fetchall()
            conx.close() # type: ignore
            
            #tomamos los datos guardados en la consulta y los agregamos 
            # como una lista en datos
            datos = []
            for row in rsUsuario:
                datos.append(list(row))

            #Regresamos la lista
            return datos
        except sqlite3.OperationalError:
            print("Error de consulta a la BD")
    
    # Metodo para actualizar un usuario por su ID
    def actualizarUsuario(self, idRe, nomRe, corRe, conRe):
        # 1. usamos una conexión para actualizar
        conx = self.conexionBD()

        # 2. Checar que el id exista y el entry contenga algo
        if not idRe:
            messagebox.showwarning("Aguas", "ID vacío")
            return
        if not nomRe or not corRe or not conRe:
            messagebox.showwarning("Aguas", "Formulario incompleto")
            return
        usuario = self.consultarUsuario(idRe)
        if not usuario:
            messagebox.showwarning("Aguas", "ID no existe en la BD")
            return

        # 3. Preparamos Cursor, Datos, QuerySQL
        cursor = conx.cursor() # type: ignore
        # Se manda a encriptar la contraseña y se agrega en el paquete de datos enviados a la BD
        conH = self.encriptarCon(conRe)
        datos = (nomRe, corRe, conH, idRe)
        qrUpdate = "update TBRegistrados set nombre=?, correo=?, contra=? where id=?"

        # 4. Ejecutar Update y cerramos conexion
        cursor.execute(qrUpdate, datos)
        conx.commit() # type: ignore
        conx.close() # type: ignore
        messagebox.showinfo("Exito", "Usuario Actualizado")
        
    def eliminarUsuario(self, idRe):
        # 1. usamos una conexión para eliminar
        conx = self.conexionBD()

        # 2. Checar que el id exista
        if not idRe:
            messagebox.showwarning("Aguas", "ID vacío")
            return
        usuario = self.consultarUsuario(idRe)
        if not usuario:
            messagebox.showwarning("Aguas", "ID no existe en la BD")
            return

        # 3. Ventana emergente de confirmación
        respuesta = messagebox.askquestion("Confirmación", "¿Estás seguro que deseas eliminar al usuario con ID "+idRe+"?")
        if respuesta == 'no':
            return

        # 4. Preparamos Cursor, Datos, QuerySQL
        cursor = conx.cursor() # type: ignore
        datos = (idRe,)
        qrDelete = "delete from TBRegistrados where id=?"

        # 5. Ejecutar Delete y cerramos conexion
        cursor.execute(qrDelete, datos)
        conx.commit() # type: ignore
        conx.close() # type: ignore
        messagebox.showinfo("Exito", "Usuario Eliminado")