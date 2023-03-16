import random

def aleatorio(letras):
    password = ''.join(random.choice(letras))
    return password