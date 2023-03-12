class datos():
    def __init__(self, M):
        self.usuario=M
    
    def Guardar(self):
        guardado1 = []
        for i in self.usuario:
            guardado1.append(i)
        return guardado1