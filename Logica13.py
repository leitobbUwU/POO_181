import random
import string

class password:
    def __init__(self, tamaño, contra):
        self.tamaño=tamaño
        self.password=contra
    
    def crafteo(self, longitud=8):
        self.tamaño = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(self.tamaño) for i in range(longitud))
        return password