import random
import string

class password:
    def __init__(self, tamaño, contra):
        self.tamaño=tamaño
        self.password=contra
    
    def crafteo(self):
        self.tamaño = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(self.tamaño) for i in range(8))
        return password