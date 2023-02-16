class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ''
        
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

class Sistema:
    def __init__(self):
        self.__listaPacientes = [ ]
        self.__numeroPacientes = len(self.__listaPacientes)

    def ingresarPaciente (self):
        print('INGRESE LOS DATOS DEL PACIENTE')
        nombre = input('Nombre: ')
        cedula = int(input('Cédula: '))
        genero = input('Genero: ')
        servicio = input('Ingrese el servicio: ')

        p = Paciente()
        p.setNombre(nombre)
        p.setCedula(cedula)
        p.setGenero(genero)
        p.setServicio(servicio)

        self.__listaPacientes.append(p)
        self.__numeroPacientes = len(self.__listaPacientes)

    def verNumeroPacientes (self):
        return self.__numeroPacientes
    
    def verDatosPaciente (self):
        cedula = int(input("Ingrese la cédula a buscar: "))
        
        for paciente in self.__listaPacientes:
            if cedula == paciente.getCedula():
                print('Nombre: ' + paciente.getNombre())
                print('Cédula: ' + str(paciente.getCedula()))
                print('Genero: ' + paciente.getGenero())
                print('Servicio: ' + paciente.getServicio())

mi_sistema = Sistema()

while True:
    menu = input('''Seleccione:
    1. Nuevo paciente.
    2. Número de pacientes.
    3. Datos de paciente.
    4. Salir.
    => ''')

    if menu == '1':
        mi_sistema.ingresarPaciente()
    elif menu == '2':
        print('Hay ' + str(mi_sistema.verNumeroPacientes()) + ' pacientes')
    elif menu == '3':
        mi_sistema.verDatosPaciente()
    elif menu == '4':
        break
    else:
        print('Opción inválida.')
