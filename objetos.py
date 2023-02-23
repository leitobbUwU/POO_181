
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


#4. Acceder a sus atributos y  etodos del cada OBJ


print("")
print("## Atributos y Metodos del Heroe: ##")
print("El personaje pertenece a la raza: " + Heroe.especie)
print("El personaje se llama: " + Heroe.nombre)
print("El personaje mide: " + str(Heroe.altura) + " metros")


Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

print("")
print("## Atributos y Metodos del Villano: ##")
print("El personaje pertenece a la raza: " + Villano.especie)
print("El personaje se llama: " + Villano.nombre)
print("El personaje mide: " + str(Villano.altura) + " metros")


Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)