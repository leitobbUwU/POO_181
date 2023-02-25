class Personaje:
    
    #Creamos al constructor
    def __init__(self, esp, nom, alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    """
    #atributos del personaje
    especie= "Humano"
    nombre= "Jhon 117"
    altura= 2.18
    """
    
    #Metodos Personaje
    
    def correr(self, status):
        if(status):
            print("El personaje "+ self.__nombre + " esta corriendo")
        else:
            print("El personaje "+ self.__nombre + " se detuvo")
            
            
    def lanzarGranada(self):
        print("Se lanzo Granada ")
        
        
    def recargarArma(self, municiones):
        cargador= 5
        cargador= cargador + municiones
        print("Quedan "+ str(cargador) + " balas")
        
    #Ejemplo de metodo privado    
    def __pensar(self):
        print("Toy pensando............")
        
    def getcorrer(self):
        return self.__especie
    
    def setespecie(self, esp):
        self.__especie=esp
        
    def getespecie(self):
        return self.__especie
        
    def getnombre(self):
        return self.__nombre
    
    def setnombre(self, nom):
        self.__nombre=nom
        
    def getaltura(self):
        return self.__altura
    
    def setaltura(self, alt):
        self.__altura=alt