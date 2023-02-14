class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""
        
    def setNombre (self, nombre):
        self.__nombre = nombre
    def setCedula (self, cedula):
        self.__cedula = cedula
    def setGenero (self, genero):
        self.__genero = genero
    def setServicio (self, servicio):
        self.__servicio = servicio
        
    def getNombre (self):
        return self.__nombre
    def getCedula (self):
        return self.__cedula
    def getGenero (self):
        return self.__genero
    def getServicio (self):
        return self.__servicio

