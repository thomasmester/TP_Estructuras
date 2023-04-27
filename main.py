from clases.Club import Club
from clases.Empleado import Empleado
from clases.Instalacion import Instalacion
from clases.Pago import Pago
from clases.Persona import Persona
from clases.Reserva import Reserva
from clases.Socio import Socio

clubes=[] #lista con OBJETOS club de la CLASE Club

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
            

c= Club('river', '1903', 'corrientes 912')
s1 = Socio('manu', 'ejbe', 'm', '16', '45422222', '1', 'manu@ejbe.com')
s2 = Socio('salva', 'luna', 'm', '19', '91255656', '2', 'salva@luna.com')
e = Empleado('fran', 'plamitos', 'f', '69', '699121312', '2', 'PLAYER', '0')

c.agregarEmpleado(e)
c.agregarSocio(s1)
c.agregarSocio(s2)
pago = Pago('1312', '13/12/2003', s1, c, '2')
c.agregarPago(pago)
c.guardarClub()

c.inicializarClub()
def menuPrincipal():
    print("1: Registrar club", '\n',
          "2: Consultar informacion general de un club", '\n',
          "3: Registrar socio en un club", '\n',
          "4: Eliminar socio en un club", '\n',
          "5: Consultar socios de un club", '\n',
          "6: Registrar instalacion en un club", '\n',
          "7: Eliminar instalacion en un club", '\n',
          "8: Consultar instalaciones de un club", '\n',
          "9: Registrar empleado en un club", '\n',
          "10: Consultar empleados de un club", '\n',
          "11: Generar pago en un club", '\n',
          "12: Eliminar pago en un club", '\n',
          "13: Consultar pagos de un club", '\n',
          "14: Crear reserva en una instalacion", '\n', 
          "15: Consultar reservas en una instalacion de un club"
          )
    opcionElegida=int(input("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar:"))
    while(opcionElegida not in range(0, 16)):
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
            return eliminarSocio()
        case 5:
            return consultarSocios()
        case 6:
            return registrarInstalacion()
        case 7:
            return eliminarInstalacion()
        case 8:
            return consultarInstalaciones()
        case 9:
            return registrarEmpleado()
        case 10:
            return consultarEmpleados()
        case 11:
            return generarPago()
        case 12:
            return eliminarPago()
        case 13:
            return consultarPagos()
        case 14:
            return crearReserva()
        case 15:
            return consultarReservas()
        
def finalizarPrograma():
    print('Sesión cerrada, programa finalizado')
    return ingreso()

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
    
def consultarInfoClub():
    nombreClub=input("Ingrese el nombre del club que quiere consultar informacion")
    existe=False
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Ese club no existe. Ingrese el nombre del club que quiere consultar informacion")
    clubes[i].presentacion()

def registrarSocio():
    nombre=input("Ingrese el nombre del socio:")
    apellido=input("Ingrese el apellido del socio:")
    sexo=input("Ingrese el sexo del socio: ")
    edad=int(input("Ingrese la edad del socio: "))
    DNI=int(input("Ingrese el DNI del socio: "))
    nroSocio=int(input("Ingrese el numero de socio: "))
    correoElectronico=input("Ingrese el correo electronico del socio: ")
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el socio: ")
    existe=False
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el socio: ")
    socio=Socio(nombre, apellido, sexo, edad, DNI, nroSocio, correoElectronico)
    clubes[aux].agregarSocio(socio)

def eliminarSocio():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un socio: ")
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un socio: ")
    nroSocio=int(input("Ingrese el numero de socio: "))
    clubes[aux].eliminarSocio(nroSocio)

def consultarSocios():
    nombreClub=input("Ingrese el club del que quiere consultar los socios: ")
    existe=False
    while (existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Nombre de club inexistente. Ingrese el club del que quiere consultar los socios: ")
    for j in range(len(clubes[aux].lista_socios)):
        print (clubes[aux].lista_socios[j].nombre, '/n')

def registrarInstalacion():
    nombre=input("Ingrese el nombre de la instalacion:")
    descripcion=input("Ingrese una descripcion de la instalacion:")
    horaApertura=input("Ingrese la hora de apertura de la instalacion: ")
    horaCiere=input("Ingrese la hora de cierre de la instalacion: ")
    codigoInstalacion=int(input("Ingrese el codigo de instalacion: "))
    nombreClub=input("Ingrese el nombre del club en el que desea registrar la instalacion: ")
    existe=False
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar la instalacion: ")
    instalacion=Socio(nombre, descripcion, horaApertura, horaCiere, codigoInstalacion, clubes[aux])
    clubes[aux].agregarInstalacion(instalacion)

def eliminarInstalacion():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar una instalacion: ")
    existe=False
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar una instalacion: ")
    codigoInstalacion=int(input("Ingrese el codigo de la instalacion que desea eliminar: "))
    clubes[aux].eliminarInstalacion(codigoInstalacion)

def consultarInstalaciones():
    nombreClub=input('Ingrese el club del que desea consultar las instalaciones')
    existe=False
    while (existe == False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar las instalaciones: ')
    for j in range(len(clubes[aux].lista_instalaciones)):
        print(clubes[aux].lista_instalaciones[j].nombre, '/n')

def registrarEmpleado():
    nombre=input("Ingrese el nombre del empleado:")
    apellido=input("Ingrese el apellido del empleado:")
    sexo=input("Ingrese el sexo del empleado: ")
    edad=int(input("Ingrese la edad del empleado: "))
    DNI=int(input("Ingrese el DNI del empleado: "))
    legajo=int(input("Ingrese el legajo del empleado: "))
    cargo=input("Ingrese el cargo del empleado: ")
    salario=float(input("Ingrese el salario actual del empleado"))
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el empleado: ")
    existe=False
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el empleado: ")
    empleado=Empleado(nombre, apellido, sexo, edad, DNI, legajo, cargo, salario)
    clubes[aux].agregarEmpleado(empleado)

def consultarEmpleados():
    nombreClub=input('Ingrese el club del que desea consultar los empleados')
    existe=False
    while (existe == False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los empleados: ')
    for j in range(len(clubes[aux].lista_empleados)):
        print(clubes[aux].lista_empleados[j].nombre, '/n')

def generarPago():
    monto=input("Ingrese el monto:")
    fecha=input("Ingrese la fecha:")
    codigoPago=int(input("Ingrese el codigo de pago: "))
    nombreClub=input("Ingrese el nombre del club en el que desea generar el pago: ")
    existe1=False
    while(existe1==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux1=i
                existe1=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea generar el pago: ")
    numeroSocio=input("Ingrese el numero de socio: ")
    existe2=False
    while(existe2==False):
        for j in range(len(clubes[aux1].lista_socios)):
            if clubes[aux1].lista_socios[j].nroSocio==numeroSocio:
                aux2=j
                existe2=True
        numeroSocio=input("Socio inexistente. Ingrese el numero de socio: ")
    pago=Pago(monto, fecha, clubes[aux1].lista_socios[aux2], clubes[aux1], codigoPago)
    clubes[aux1].agregarPago(pago)

def eliminarPago():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un pago: ")
    existe=False
    while(existe==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un pago: ")
    nroPago=int(input("Ingrese el numero de pago del pago que desea eliminar: "))
    clubes[aux].eliminarPago(nroPago)

def consultarPagos():
    nombreClub=input('Ingrese el club del que desea consultar los pagos')
    existe=False
    while (existe == False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los pagos: ')
    for j in range(len(clubes[aux].lista_pagos)):
        print(clubes[aux].lista_pagos[j].monto, '/n')

def crearReserva():
    fechaReserva=input("Ingrese la fecha de reserva:")
    horaReserva=input("Ingrese la hora de reserva:")
    nroReserva=int(input("Ingrese el numero de reserva: "))
    nombreClub=input("Ingrese el nombre del club en el que desea realizar la reserva: ")
    existe1=False
    while(existe1==False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux1=i
                existe1=True
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea realizar la reserva: ")
    codigo=input("Ingrese el codigo de la instalacion que desea reservar: ")
    existe2=False
    while(existe2==False):
        for j in range(len(clubes[aux1].lista_instalaciones)):
            if clubes[aux1].lista_instalaciones[j].codigoInstalacion == codigo:
                aux2=j
                existe2=True
        codigo=input("Instalacion inexistente. Ingrese el codigo de la instalacion que desea reservar: ")
    reserva=Reserva(fechaReserva, horaReserva, nroReserva)
    clubes[aux1].lista_instalaciones[aux2].agregarReserva(reserva)

def consultarReservas():
    nombreClub=input('Ingrese el nombre del club del que desea consultar las reservas de una instalacion')
    existe1=False
    while (existe1 == False):
        for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux1=i
                existe1=True
        nombreClub=input('Nombre del club inexistente. Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
    codigo=int(input('Ingrese el codigo de la instalacion de la cual desea consultar las reservas: '))
    existe2=False
    while (existe2 == False):
        for j in range(len(clubes[aux1].lista_instalaciones)):
            if clubes[aux1].lista_instalaciones[j].codigoInstalacion==codigo:
                aux2=j
                existe2=True
        codigo=input('Codigo de reserva inexistente. Ingrese el codigo de la instalacion de la cual desea consultar las reservas: ')
    for r in range(len(clubes[aux1].lista_instalaciones[aux2].lista_reservas)):
        print( clubes[aux1].lista_instalaciones[aux2].lista_reservas[r].nroReserva, '/n')