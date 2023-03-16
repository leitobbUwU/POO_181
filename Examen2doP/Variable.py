import random

def aleatorio(string):
    letras = string.ascii_lowercase
    password = ''.join(random.choice(letras) for _ in range(2))
    return password