class Login:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def verificar_usuario(self):
        # Aquí se puede colocar la lógica para verificar si el usuario y la contraseña son válidos
        # Por ejemplo, si el usuario está en una base de datos y la contraseña coincide con la almacenada
        
        # En este caso, simplemente se comprueba si el usuario es "ejemplo" y la contraseña es "password"
        if self.usuario == "ejemplo" and self.contraseña == "password":
            return True
        else:
            return False