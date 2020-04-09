#------------------------------------Clase Socio
class Socio:
    def __init__(self, dni, nombre, telefono, domicilio):
        self.dni=dni
        self.nombre=nombre
        self.telefono=telefono
        self.domicilio=domicilio
        
    def __str__(self):
       return 'DNI: {0}\nNombre: {1}\nTeléfono: {2}\nDomicilio: {3}\n'\
           .format(self.dni,self.nombre,self.telefono,self.domicilio)
#Se arreglo la clase pelicula con alquilada
class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo=titulo
        self.genero=genero
        self.alquilada=None
    
    def __str__(self):
         cadena='Titulo: {0}\nGénero: {1}'.format(self.titulo,self.genero)
         if self.alquilada==None:
            cadena=cadena+' Disponible'
         else:
            cadena=cadena+'Alquilada a: {0}\n'.format(self.alquilada)
         return cadena
#------------------------------------------Clase Videoclub
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
        
    def baja_socio(self,dni):
        for  i in range(len(self.socios)):
            if self.socios[i].dni==dni:
                del self.socios[i]
                break
            
    def alta_pelicula(self,pelicula):
        self.peliculas.append(pelicula)
    
    def baja_pelicula(self,titulo):
        for  i in range(len(self.peliculas)):
            if self.peliculas[i].titulo==titulo:
                del self.peliculas[i]
                break
        
    def contiene_pelicula(self,titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo==titulo:
                return True
        return False
    
    def alquilar_pelicula(self, titulo,dni):
        for pelicula in self.peliculas:
            if pelicula.titulo==titulo: 
                if pelicula.alquilada==None:
                    pelicula.alquilada=dni
                    return True
                else:
                    return False
#---------------------------------------Creacion de funciones
#creacion de la funcion menu

def menu():
    
    print("********************VIDEOCLUB********************")
    print("1) Dar de alta un socio")
    print("2) Dar de baja un socio")   
    print("3) Dar de alta un nueva pelicula")
    print("4) Dar de baja una pelicula")
    print("5) Alquilar pelicula")
    print("6) Salir")
    opcion=int(input("Ingrese opcion: "))
    while opcion>6 or opcion<1:
        opcion=int(input("Vuelva a ingresar una opcion correcta: "))   
    return opcion

#Creacion de la funcion nuevo_socio
def nuevo_socio():
    dni=input("Ingrese su DNI: ")
    nombre=input("Ingrese su nombre: ")
    telefono=input("Ingrese su telofono: ")
    domicilio=input("Ingrese su domicilio: ")
    
    return Socio(dni,nombre,telefono,domicilio)

def nuevo_pelicula():
    titulo=input("Ingrese Titulo: ")
    genero=input("Ingrese Genero: ")
    return Pelicula(titulo,genero)

#El socio devuelto por nuevo_socio puede haber sido dado de alta previamente en el videoclub,
#con lo que no sería procedente darlo de alta ahora. A



#Creando instancia de la clase Videoclub
videoclub=Videoclub()
opcion=menu()
while opcion!=6:
    if opcion==1:
        print("\nAlta de socio")
        socio=nuevo_socio()
        if videoclub.contiene_socio(socio.dni):
            print("Ya existía un socio con DNI ",socio.dni,"\n")
        else:
            print("Socio Agregado\n")
            videoclub.alta_socio(socio)#Recibe como parametro un objeto
    elif opcion==2:
        print("\nBaja de socio")
        dni=input("DNI: ")
        if videoclub.contiene_socio(dni):
            videoclub.baja_socio(dni)
            print("Socio con DNI: ",dni," dado de baja\n")
        else:
            print("No existe ningun socio con DNI: ",dni,"\n")
    elif opcion==3:
        print("\nAlta de pelicula")
        pelicula=nuevo_pelicula()
        if videoclub.contiene_pelicula(pelicula.titulo):
            print("Ya existia una pelicula con titulo: ",pelicula.titulo,"\n")
        else:
            videoclub.alta_pelicula(pelicula)
            print("Pelicula agragada\n")
            
    elif opcion==4:
        print("\nBaja de pelicula")
        titulo=input("Ingrese titulo de la pelicula: ")
        if videoclub.contiene_pelicula(titulo):
            videoclub.baja_pelicula(titulo)
            print("Pelicula con titulo:",titulo, "dado de baja\n")
        else:
            print("No existe ninguna pelicula con ese titulo:",pelicula,"\n")
    elif opcion==5:
        print("\nAlquiler de pelicula")
        titulo=input("Titulo de la pelicula: ")
        dni=input("DNI del socio: ")
        hay_pelicula=videoclub.contiene_pelicula(titulo)
        hay_socio=videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            videoclub.alquilar_pelicula(titulo, dni)
            print("Pelicula ",titulo," alquilada al DNI: ",dni,"\n"  )
        else:
            if not hay_pelicula:
                print("No hay pelicula titulada ",titulo)
            if not hay_socio:
                print("No hay socio con DNI: ",dni)
            print("\n")    
    opcion=menu()
    
        