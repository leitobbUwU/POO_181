class Personaje:
    
    #Creamos al constructor
    def __init__(self, esp, nom, alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    """
    #atributos del personaje
    especie= "Humano"
    nombre= "Jhon 117"
    altura= 2.18
    """
    
    #Metodos Personaje
    
    def correr(self, status):
        if(status):
            print("El personaje "+ self.nombre + " esta corriendo")
        else:
            print("El personaje "+ self.nombre + " se detuvo")
            
            
    def lanzarGranada(self):
        print("Se lanzo Granada ")
        
        
    def recargarArma(self, municiones):
        cargador= 5
        cargador= cargador + municiones
        print("Quedan "+ str(cargador) + " balas")