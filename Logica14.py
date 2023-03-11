


class datos():
    def __init__(self, M):
        self.usuario=M
    
    def Guardar(self):
        asx = []
        for i in self.usuario:
            asx.append(i)
        return asx