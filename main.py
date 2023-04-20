from clases.Actividad import Actividad
from clases.Club import Club
from clases.Empleado import Empleado
from clases.Evento import Evento
from clases.Instalacion import Instalacion
from clases.Pago import Pago
from clases.Persona import Persona
from clases.Reserva import Reserva
from clases.Socio import Socio

clubes=[]

def ingreso(archivo):
    archivo = open(archivo,"a",encoding="utf-8")
    print("1. Registrarse",'\n',"2. Iniciar sesión",'\n')
    opcion = input("Ingrese la opción: ")
    while opcion != 1 and opcion != 2:
        opcion = input("Ingrese una opción valida: ")
    if opcion == 1:
        usuario = input("Ingrese usuario: ")
        contrasenia = input("Ingrese contraseña: ")
        archivo.write(usuario + " " + contrasenia + '\n')
    else:
        lista = []
        for linea in archivo:
            uc = linea[:-1].split(" ")
            lista.append(uc)
        for i in range(len(lista)):
            if lista[i][0] == usuario:
                return lista[i][1] == contrasenia
            
def menuPrincipal():
    print("1: Registrar club", '\n',
          "2: Consultar informacion general de un club", '\n',
          "3: Registrar socio en un club", '\n',
          "4: Consultar socios de un club", '\n',
          "5: Registrar instalacion en un club", '\n',
          "6: Consultar instalaciones de un club", '\n',
          "7: Registrar empleado en un club", '\n',
          "8: Consultar empleados de un club", '\n',
          "9: Generar pago en un club", '\n',
          "10: Consultar pagos de un club", '\n',
          "11: Crear reserva en una instalacion", '\n', 
          "12: Consultar reservas en una instalacion de un club", '\n',
          "13: Crear actividad en un club", '\n', 
          "14: Consultar actividades de un club", '\n',
          )
    opcionElegida=int(input("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finaliar:"))
    while(opcionElegida!=1 and opcionElegida!=2 and opcionElegida!=3 and opcionElegida!=4 and opcionElegida!=5 and opcionElegida!=6 and opcionElegida!=7 and opcionElegida!=8 and opcionElegida!=9 and opcionElegida!=10 and opcionElegida!=11 and opcionElegida!=12 and opcionElegida!=13 and opcionElegida!=14 and opcionElegida!=0):
        opcionElegida=int(input("La opcion elegida no es valida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finaliar:"))
    match opcionElegida:
        case 0:
            return finalizarPrograma()
        case 1:
            return registrarClub()
        case 2:
            return consultarInfoClub()
        case 3:
            return registrarSocio()
        case 4:
            return consultarSocios()
        case 5:
            return registrarInstalacion()
        case 6:
            return consultarInstalaciones()
        case 7:
            return registrarEmpleado()
        case 8:
            return consultarEmpleados()
        case 9:
            return generarPago()
        case 10:
            return consultarPagos()
        case 11:
            return crearReserva()
        case 12:
            return consultarReservas()
        case 13:
            return crearActividad()
        case 14:
            return consultarActividades()
        
def finalizarPrograma():
    print('Sesión cerrada, programa finalizado')

def registrarClub():
    nombre=input("Ingrese el nombre del club: ")
    while (nombre==""):
        nombre=input("Ingrese un nombre de club valido: ")
    anioFundacion=int(input("Ingrese el año de fundacion: "))
    while (anioFundacion <=0):
        anioFundacion=int(input("Ingrese un año de fundacion valido: "))
    direccion=input("Ingrese la direccion: ")
    while (direccion==""):
        direccion=input("Ingrese una direccion de club valida: ")
    try:
        club = Club(nombre, anioFundacion, direccion)
    except ValueError:
        print("Ese nombre ya existe")
        return menuPrincipal()
    clubes.append(club)
    
def consultarInfoClub(Club):
    nombre=input("Ingrese el nombre del club que quiere consultar informacion o 0 para elegir otra opcion del menu")
    while(nombre not in Club.lista_nombres and nombre!="0"):
        nombre=input("Ese club no existe. Ingrese el nombre del club que quiere consultar informacion o 0 para elegir otra opcion del menu")
    if(nombre=="0"):
        return menuPrincipal()
    else:
        for i in range(len(clubes)):
            if clubes[i].nombre==nombre:
                clubes[i].presentacion()

def registrarSocio():
    nombre=input("Ingrese el nombre del socio:")
    apellido=input("Ingrese el apellido del socio:")
    sexo=input("Ingrese el sexo del socio: ")
    edad=int(input("Ingrese la edad del socio: "))
    DNI=int(input("Ingrese el DNI del socio: "))
    nroSocio=int(input("Ingrese el numero de socio: "))
    correoElectronico=input("Ingrese el correo electronico del socio: ")
    club=input("Ingrese el nombre del club en el que desea registrar el socio: ")
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==club:
                existe=True
        club=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el socio: ")
    socio=Socio(nombre, apellido, sexo, edad, DNI, nroSocio, correoElectronico)
    for i in range(len(clubes)):
        if clubes[i].nombre==club:
            clubes[i].agregarSocio(socio)

def consultarSocios():
    club=input("Ingrese el club del que quiere consultar los socios: ")
    while (club not in clubes):
        club=input("Nombre de club inexistente. Ingrese el club del que quiere consultar los socios: ")
    for i in range(len(clubes)):
        if clubes[i].nombre==club:
            for j in range(len(clubes[i].lista_socios)):
                print (clubes[i].lista_socios[j].nombre)

def consultarInstalaciones():
    club=input('Ingrese el club del que desea consultar las instalaciones')
    while (club not in clubes):
        club=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los socios: ')
    for i in range(len(clubes)):
        if clubes[i].nombre==club:
            for j in range(len(clubes[i].instalaciones)):
                print(clubes[i].lista_instalaciones[j].nombre)