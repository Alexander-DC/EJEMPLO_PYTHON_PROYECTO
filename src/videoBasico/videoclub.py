class Socio:
    def __init__(self, dni, nombre, telefono, domicilio):
        self.dni=dni
        self.nombre=nombre
        self.telefono=telefono
        self.domicilio=domicilio
        
    def __str__(self):
       return 'DNI: {0}\nNombre: {1}\nTeléfono: {2}\nDomicilio: {3}\n'\
           .format(self.dni,self.nombre,self.telefono,self.domicilio)
    
class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo=titulo
        self.genero=genero
    
    def __str__(self):
        return 'Titulo: {0}\nGénero: {1}'.format(self.titulo,self.genero)

#Clase Videoclub que mantega y gestione las listas de socios y peliculas
class Videoclub:
    def __init__(self):
        self.socios=[]
        self.peliculas=[]
    
    def contiene_socio(self,dni):
        for socio in self.socios:
            if socio.dni==dni:
                return True
        return False
    
    def alta_socio(self,socio):
        self.socios.append(socio)
#Creacion de funciones
#creacion de la funcion menu

def menu():
    print("***VIDEOCLUB***")
    print("1) Dar de alta un socio")
    print("2) Dar de baja un socio")   
    print("3) Dar de alta un nueva pelicula")
    print("4) Dar de baja una pelicula")
    print("5) Salir")
    opcion=int(input("Ingrese opcion: "))
    while opcion>5 or opcion<1:
        opcion=int(input("Vuelva a ingresar una opcion correcta: "))   
    return opcion

def nuevo_socio():
    dni=input("Ingrese su DNI: ")
    nombre=input("Ingrese su nombre: ")
    telefono=input("Ingrese su telofono: ")
    domicilio=input("Ingrese su domicilio: ")
    
    return Socio(dni,nombre,telefono,domicilio)

#El socio devuelto por nuevo_socio puede haber sido dado de alta previamente en el videoclub,
#con lo que no sería procedente darlo de alta ahora. A