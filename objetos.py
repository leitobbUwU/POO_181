
#1. importar la clase
from personaje import *

#2. Solicitar atributos para el objeto
print(" ")
print("### Solicitud de datos Heroe ###")
espH= input("Escribe la especie del Heroe: ")
nomH= input("Escribe el nombre del Heroe: ")
altH= float(input("Escribe la altura del Heroe: "))
cargaH= int(input("Cuantas balas se recargan al Heroe: "))

print(" ")
print("### Solicitud de datos Villano ###")
espV= input("Escribe la especie del Villano: ")
nomV= input("Escribe el nombre del Villano: ")
altV= float(input("Escribe la altura del Villano: "))
cargaV= int(input("Cuantas balas se recargan al Villano: "))

#3. Creamos 2 objetos
Heroe= Personaje(espH, nomH, altH)
Villano = Personaje(espV, nomV, altV)

#Ejemplo del metodo set
Heroe.setnombre("Jhon 117")

#4. Acceder a sus atributos y  etodos del cada OBJ

print("")
print("## Atributos y Metodos del Heroe: ##")
print("El personaje pertenece a la raza: " + Heroe.getespecie())
print("El personaje se llama: " + Heroe.getnombre())
print("El personaje mide: " + str(Heroe.getaltura()) + " metros")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

#Ejemplo de lo que no se debe de hacer
#Heroe.__pensar()

print("")
print("## Atributos y Metodos del Villano: ##")
print("El personaje pertenece a la raza: " + Villano.getespecie())
print("El personaje se llama: " + Villano.getnombre())
print("El personaje mide: " + str(Villano.getaltura()) + " metros")


Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)