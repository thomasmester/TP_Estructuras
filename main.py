from clases.Club import Club
from clases.Empleado import Empleado
from clases.Instalacion import Instalacion
from clases.Pago import Pago
from clases.Persona import Persona
from clases.Reserva import Reserva
from clases.Socio import Socio

#c= Club('river', '1903', 'corrientes 912')
clubes=[] #lista con OBJETOS club de la CLASE Club

def ingreso(archivo):
    print(" 1. Registrarse",'\n',"2. Iniciar sesión",'\n')
    opcion = input("Ingrese la opción: ")
    while opcion != "1" and opcion != "2":
        opcion = input("Ingrese la opción: ")
    usuario = input("Ingrese usuario: ")
    contrasenia = input("Ingrese contraseña: ")
    if opcion == "1":
        archivo = open(archivo,"a",encoding="utf-8")
        archivo.write(usuario + " " + contrasenia + '\n')
        archivo.close()
        menuPrincipal()
    else:
        archivo = open(archivo,"r",encoding="utf-8")
        lista = []
        for linea in archivo:
            uc = linea[:-1].split(" ")
            lista.append(uc)
        for i in range(len(lista)):
            if lista[i][0] == usuario:
                if lista[i][1] == contrasenia:
                    menuPrincipal()
                else:
                    print("Usuario o contraseña incorrectos")
        archivo.close()
            
'''s1 = Socio('manu', 'ejbe', 'm', '16', '45422222', '1', 'manu@ejbe.com')
s2 = Socio('salva', 'luna', 'm', '19', '91255656', '2', 'salva@luna.com')
e = Empleado('fran', 'plamitos', 'f', '69', '699121312', '2', 'PLAYER', '0')
c.agregarEmpleado(e)
c.agregarSocio(s1)
c.agregarSocio(s2)
pago = Pago('1312', '13/12/2003', '1', '2')
c.agregarPago(pago)
c.guardarClub()'''

#c.inicializarClub()

def menuPrincipal():
    termina=False
    while (not termina):
        print("Menu principal", '\n', 
          "1: Registrar club", '\n',
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
        opcionElegida=int(input("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: "))
        while(opcionElegida not in range(0, 16)):
            opcionElegida=int(input("La opcion elegida no es valida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finaliar:"))
        match opcionElegida:
            case 0:
                finalizarPrograma()
                termina=True
            case 1:
                registrarClub()
            case 2:
                consultarInfoClub()
            case 3:
                registrarSocio()
            case 4:
                eliminarSocio()
            case 5:
                consultarSocios()
            case 6:
                registrarInstalacion()
            case 7:
                eliminarInstalacion()
            case 8:
                consultarInstalaciones()
            case 9:
                registrarEmpleado()
            case 10:
                consultarEmpleados()
            case 11:
                generarPago()
            case 12:
                eliminarPago()
            case 13:
                consultarPagos()
            case 14:
                crearReserva()
            case 15:
                consultarReservas()

def verificarExistenciaClub(nombreClub):
    existe=False
    aux=-1
    for i in range(len(clubes)):
            if clubes[i].nombre==nombreClub:
                aux=i
                existe=True
    datos=[existe, aux]
    return datos

def verificarExistenciaInstalacion(codigo, indiceClub):
    existe=False
    aux=-1
    for i in range(len(clubes[indiceClub].lista_instalaciones)):
            if clubes[indiceClub].lista_instalaciones[i]==codigo:
                aux=i
                existe=True
    datos=[existe, aux]
    return datos

def finalizarPrograma():
    print('Sesión cerrada, programa finalizado')
    ingreso("archivo.txt")

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
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Ese club no existe. Ingrese el nombre del club que quiere consultar informacion")
        datos=verificarExistenciaClub(nombreClub)
    clubes[datos[1]].presentacion()

def registrarSocio():
    nombre=input("Ingrese el nombre del socio:")
    apellido=input("Ingrese el apellido del socio:")
    sexo=input("Ingrese el sexo del socio: ")
    edad=int(input("Ingrese la edad del socio: "))
    while (edad <= 0):
        edad=int(input("Edad invalida. Ingrese la edad del socio: "))
    DNI=int(input("Ingrese el DNI del socio: "))
    while (DNI <= 0):
        DNI=int(input("DNI invalido. Ingrese el DNI del socio: "))
    nroSocio=int(input("Ingrese el numero de socio: "))
    correoElectronico=input("Ingrese el correo electronico del socio: ")
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el socio: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el socio: ")
        datos=verificarExistenciaClub(nombreClub)
    socio=Socio(nombre, apellido, sexo, edad, DNI, nroSocio, correoElectronico)
    clubes[datos[1]].agregarSocio(socio)

def eliminarSocio():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un socio: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un socio: ")
        datos=verificarExistenciaClub(nombreClub)
    nroSocio=int(input("Ingrese el numero de socio: "))
    clubes[datos[1]].eliminarSocio(nroSocio)

def consultarSocios():
    nombreClub=input("Ingrese el club del que quiere consultar los socios: ")
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0]==False):
        nombreClub=input("Nombre de club inexistente. Ingrese el club del que quiere consultar los socios: ")
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_socios)):
        print (clubes[datos[1]].lista_socios[j].nombre, '/n')

def registrarInstalacion():
    nombre=input("Ingrese el nombre de la instalacion:")
    descripcion=input("Ingrese una descripcion de la instalacion:")
    horaApertura=input("Ingrese la hora de apertura de la instalacion: ")
    horaCiere=input("Ingrese la hora de cierre de la instalacion: ")
    codigoInstalacion=int(input("Ingrese el codigo de instalacion: "))
    while (codigoInstalacion <= 0):
        codigoInstalacion=int(input("Ingrese un codigo de instalacion valido: "))
    nombreClub=input("Ingrese el nombre del club en el que desea registrar la instalacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar la instalacion: ")
        datos=verificarExistenciaClub(nombreClub)
    instalacion=Instalacion(nombre, descripcion, horaApertura, horaCiere, codigoInstalacion, nombreClub)
    clubes[datos[1]].agregarInstalacion(instalacion)

def eliminarInstalacion():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar una instalacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar una instalacion: ")
        datos=verificarExistenciaClub(nombreClub)
    codigoInstalacion=int(input("Ingrese el codigo de la instalacion que desea eliminar: "))
    clubes[datos[1]].eliminarInstalacion(codigoInstalacion)

def consultarInstalaciones():
    nombreClub=input('Ingrese el club del que desea consultar las instalaciones')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar las instalaciones: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_instalaciones)):
        print(clubes[datos[1]].lista_instalaciones[j].nombre, '/n')

def registrarEmpleado():
    nombre=input("Ingrese el nombre del empleado:")
    apellido=input("Ingrese el apellido del empleado:")
    sexo=input("Ingrese el sexo del empleado: ")
    edad=int(input("Ingrese la edad del empleado: "))
    while (edad <= 0):
        edad=int(input("Edad invalida. Ingrese la edad del empleado: "))
    DNI=int(input("Ingrese el DNI del empleado: "))
    while (DNI <= 0):
        DNI=int(input("DNI invalido. Ingrese el DNI del empleado: "))
    legajo=int(input("Ingrese el legajo del empleado: "))
    while (legajo <= 0):
        legajo=int(input("Legajo invalido. Ingrese el legajo del empleado: "))
    cargo=input("Ingrese el cargo del empleado: ")
    salario=float(input("Ingrese el salario actual del empleado"))
    while (salario <= 0):
        salario=float(input("Salario invalido. Ingrese el salario del empleado: "))
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el empleado: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el empleado: ")
        datos=verificarExistenciaClub(nombreClub)
    empleado=Empleado(nombre, apellido, sexo, edad, DNI, legajo, cargo, salario)
    clubes[datos[1]].agregarEmpleado(empleado)

def consultarEmpleados():
    nombreClub=input('Ingrese el club del que desea consultar los empleados')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los empleados: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_empleados)):
        print(clubes[datos[1]].lista_empleados[j].nombre, '/n')

def generarPago():
    monto=float(input("Ingrese el monto:"))
    while (monto <= 0):
        monto=float(input("Monto invalido. Ingrese el monto:"))
    fecha=input("Ingrese la fecha:")
    codigoPago=int(input("Ingrese el codigo de pago: "))
    nombreClub=input("Ingrese el nombre del club en el que desea generar el pago: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea generar el pago: ")
        datos=verificarExistenciaClub(nombreClub)
    numeroSocio=input("Ingrese el numero de socio: ")
    pago=Pago(monto, fecha, numeroSocio, codigoPago)
    clubes[datos[1]].agregarPago(pago)

def eliminarPago():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un pago: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un pago: ")
        datos=verificarExistenciaClub(nombreClub)
    nroPago=int(input("Ingrese el numero de pago del pago que desea eliminar: "))
    clubes[datos[1]].eliminarPago(nroPago)

def consultarPagos():
    nombreClub=input('Ingrese el club del que desea consultar los pagos')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los pagos: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_pagos)):
        print(clubes[datos[1]].lista_pagos[j].monto, '/n')

def crearReserva():
    fechaReserva=input("Ingrese la fecha de reserva:")
    horaReserva=input("Ingrese la hora de reserva:")
    nroReserva=int(input("Ingrese el numero de reserva: "))
    while (nroReserva <= 0):
        nroReserva=int(input("Numero de reserva invalido. Ingrese el numero de reserva: "))
    nombreClub=input("Ingrese el nombre del club en el que desea realizar la reserva: ")
    datos1=verificarExistenciaClub(nombreClub)
    while(datos1[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea realizar la reserva: ")
        datos1=verificarExistenciaClub(nombreClub)
    codigo=input("Ingrese el codigo de la instalacion que desea reservar: ")
    datos2=verificarExistenciaInstalacion(codigo, datos1[1])
    while(datos2[0]==False):
        codigo=input("Instalacion inexistente. Ingrese el codigo de la instalacion que desea reservar: ")
        datos2=verificarExistenciaInstalacion(codigo, datos1[1])
    reserva=Reserva(fechaReserva, horaReserva, nroReserva)
    clubes[datos1[1]].lista_instalaciones[datos2[1]].agregarReserva(reserva)

def consultarReservas():
    nombreClub=input('Ingrese el nombre del club del que desea consultar las reservas de una instalacion')
    datos1=verificarExistenciaClub(nombreClub)
    while (datos1[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
        datos1=verificarExistenciaClub(nombreClub)
    codigo=int(input('Ingrese el codigo de la instalacion de la cual desea consultar las reservas: '))
    datos2=verificarExistenciaInstalacion(codigo, datos1[1])
    while (datos2[0] == False):
        codigo=input('Codigo de reserva inexistente. Ingrese el codigo de la instalacion de la cual desea consultar las reservas: ')
        datos2=verificarExistenciaInstalacion(codigo, datos1[1])
    for r in range(len(clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas)):
        print( clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas[r].nroReserva, '/n')

ingreso("archivo.txt")