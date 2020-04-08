class Socio:
    def __init__(self, dni, nombre, telefono, domicilio):
        self.dni=dni
        self.nombre=nombre
        self.telefono=telefono
        self.domicilio=domicilio
        
    def __str__(self):
       return 'DNI: {0}\nNombre: {1}\nTeléfono: {2}\nDomicilio: {3}\n'\
           .format(self.dni,self.nombre,self.telefono,self.domicilio)
    
