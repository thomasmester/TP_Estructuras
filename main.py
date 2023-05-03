from clases.Club import Club, splitearLista
from clases.Empleado import Empleado
from clases.Instalacion import Instalacion
from clases.Pago import Pago
from clases.Persona import Persona
from clases.Reserva import Reserva
from clases.Socio import Socio

#c= Club('river', '1903', 'corrientes 912')
clubes=[] #lista con OBJETOS club de la CLASE Club

def ingreso(archivo):
    print("Bienvenido. Seleccione alguna de las siguientes opciones", '\n',
          "1. Registrarse",'\n',
          "2. Iniciar sesión")
    opcion = verificarNumeroInput("Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")
    while opcion not in range(1,3):
        print("Opcion invalida")
        opcion = verificarNumeroInput("Ingrese la opción: ", "Opcion invalida. Ingrese la opcion que desea elegir: ")
    usuario = input("Ingrese usuario: ")
    txt = open(archivo,"r",encoding="utf-8")
    matrizUsuCon = []
    for linea in txt:
        uc = linea[:-1].split(" ")
        matrizUsuCon.append(uc)
    txt.close()
    match opcion:
        case 1:
            esta=True
            while esta==True:
                encontro = False
                for i in range(len(matrizUsuCon)):
                    if matrizUsuCon[i][0] == usuario:
                        encontro=True
                if encontro == True:
                    usuario = input("Este nombre de usuario ya existe, utilice otro: ")
                else:
                    esta=False
            contrasenia = input("Ingrese contraseña: ")
            txt = open(archivo,"a",encoding="utf-8")
            txt.write(usuario + " " + contrasenia + '\n')
            txt.close()
            menuPrincipal()
        case 2:
            sesionIniciada = False
            while (sesionIniciada==False):
                contrasenia = input("Ingrese contraseña: ")
                for i in range(len(matrizUsuCon)):
                    if matrizUsuCon[i][0] == usuario and matrizUsuCon[i][1]==contrasenia:
                        sesionIniciada = True
                if sesionIniciada == False:
                    print("Usuario o contraseña incorrectos. Ingrese los datos nuevamente:")
                    usuario = input("Ingrese usuario: ")
            menuPrincipal()
            
'''s1 = Socio('manu', 'ejbe', 'm', '16', '45422222', '1', 'manu@ejbe.com')
s2 = Socio('salva', 'luna', 'm', '19', '91255656', '2', 'salva@luna.com')
e = Empleado('fran', 'plamitos', 'f', '69', '699121312', '2', 'PLAYER', '0')
c.agregarEmpleado(e)
c.agregarSocio(s1)
c.agregarSocio(s2)
i = Instalacion('cancha', 'cancha de f5', '10:30', '18:00', '1')
r = Reserva('17/12', '14:00', '2')
i.agregarReserva(r)
pago = Pago('1312', '13/12/2003', '1', '2')
c.agregarPago(pago)
c.guardarClub()'''

#c.inicializarClub()

def menuPrincipal():
    inicializarListaClubes()
    for c in clubes:
        c.incializarClub()
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
        opcionElegida=verificarNumeroInput("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ", "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
        while opcionElegida not in range(0,16):
            print("Opcion invalida")
            opcionElegida=verificarNumeroInput("Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ", "Opcion invalida. Ingrese el numero segun la opcion que quiera elegir o 0 para cerrar sesion y finalizar: ")
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

def guardarListaClubes():
    club_text = ''
    for c in clubes:
        club_text += c.nombre + ',' + c.anioFundacion + ',' + c.direccion + '|'
    with open("clubes.txt", "w") as f:
            f.write(club_text)

def inicializarListaClubes():
    with open('clubes.txt', 'r') as d:
        text = d.read()
        clubes = text.split('|')
        clubes = splitearLista(clubes, ',')
        for c in clubes:
            clubes.append(Club(*c))

def verificarExistenciaInstalacion(codigo, indiceClub):
    existe=False
    aux=-1
    for i in range(len(clubes[indiceClub].lista_instalaciones)):
            if clubes[indiceClub].lista_instalaciones[i]==codigo:
                aux=i
                existe=True
    datos=[existe, aux]
    return datos

def verificarNumeroInput (texto1, texto2):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            if varInt > 0:
                break
            else:
                print("Ingreso invalido. Por favor, inténtelo de nuevo.")
        except ValueError:
            print(texto2)
    return varInt

def verificarInputVacio (texto1, texto2):
    data=input(texto1)
    while (data==""):
        data=input(texto2)
    return data

def finalizarPrograma():
    print('Sesión cerrada, programa finalizado')
    ingreso("archivo.txt")
    for c in clubes:
        c.guardarClub()
    guardarListaClubes()

def registrarClub():
    nombre=verificarInputVacio("Ingrese el nombre del club: ", "Ingrese un nombre de club valido: ")
    anioFundacionInt=verificarNumeroInput("Ingrese el año de fundacion: ", "Ingrese un año de fundacion valido: ")
    direccion=verificarInputVacio("Ingrese la direccion: ", "Ingrese una direccion de club valida: ")
    try:
        club = Club(nombre, anioFundacionInt, direccion)
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
    nombre=verificarInputVacio("Ingrese el nombre del socio:", "Ingrese un nombre valido: ")
    apellido=verificarInputVacio("Ingrese el apellido del socio:", "Ingrese un apellido valido: ")
    sexo=verificarInputVacio("Ingrese el sexo del socio: ", "Ingrese un sexo valido: ")
    edadInt=verificarNumeroInput("Ingrese la edad del socio: ", "Edad invalida. Ingrese la edad del socio: ")
    dniInt=verificarNumeroInput("Ingrese el DNI del socio: ", "DNI invalido. Ingrese el DNI del socio: ")
    nroSocioInt=verificarNumeroInput("Ingrese el numero de socio: ", "Numero de socio invalido. Ingrese el numero de socio: ")
    correoElectronico=verificarInputVacio("Ingrese el correo electronico del socio: ", "Ingrese un correo electronico valido: ")
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el socio: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el socio: ")
        datos=verificarExistenciaClub(nombreClub)
    socio=Socio(nombre, apellido, sexo, edadInt, dniInt, nroSocioInt, correoElectronico)
    clubes[datos[1]].agregarSocio(socio)

def eliminarSocio():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un socio: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un socio: ")
        datos=verificarExistenciaClub(nombreClub)
    nroSocioInt=verificarNumeroInput("Ingrese el numero de socio del socio que desea eliminar: ", "Numero de socio invalido. Intente nuevamente")
    clubes[datos[1]].eliminarSocio(nroSocioInt)

def consultarSocios():
    nombreClub=input("Ingrese el club del que quiere consultar los socios: ")
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0]==False):
        nombreClub=input("Nombre de club inexistente. Ingrese el club del que quiere consultar los socios: ")
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_socios)):
        print (clubes[datos[1]].lista_socios[j].nombre, '\n')

def registrarInstalacion():
    nombre=verificarInputVacio("Ingrese el nombre de la instalacion: ", "Ingrese un nombre valido: ")
    descripcion=verificarInputVacio("Ingrese la descripcion de la instalacion: ", "Ingrese una descripcion valida: ")
    horaApertura=verificarInputVacio("Ingrese la hora de apertura de la instalacion: ", "Ingrese un horario valido: ")
    horaCierre=verificarInputVacio("Ingrese la hora de cierre de la instalacion: ", "Ingrese un horario valido: ")
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea registrar: ","Ingrese un codigo de instalacion valido: " )    
    nombreClub=input("Ingrese el nombre del club en el que desea registrar la instalacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar la instalacion: ")
        datos=verificarExistenciaClub(nombreClub)
    instalacion=Instalacion(nombre, descripcion, horaApertura, horaCierre, codigoInstalacionInt, nombreClub)
    clubes[datos[1]].agregarInstalacion(instalacion)

def eliminarInstalacion():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar una instalacion: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar una instalacion: ")
        datos=verificarExistenciaClub(nombreClub)
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea eliminar: ","Ingrese un codigo de instalacion valido: ") 
    clubes[datos[1]].eliminarInstalacion(codigoInstalacionInt)

def consultarInstalaciones():
    nombreClub=input('Ingrese el club del que desea consultar las instalaciones: ')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar las instalaciones: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_instalaciones)):
        print(clubes[datos[1]].lista_instalaciones[j].nombre, '\n')

def registrarEmpleado():
    nombre=verificarInputVacio("Ingrese el nombre del empleado:", "Ingrese un nombre valido: ")
    apellido=verificarInputVacio("Ingrese el apellido del empleado:", "Ingrese un apellido valido: ")
    sexo=verificarInputVacio("Ingrese el sexo del empleado: ", "Ingrese un sexo valido: ")
    edadInt=verificarNumeroInput("Ingrese la edad del empleado: ", "Edad invalida. Ingrese la edad del empleado: ")
    dniInt=verificarNumeroInput("Ingrese el DNI del empleado: ", "DNI invalido. Ingrese el DNI del empleado: ")
    legajoInt=verificarNumeroInput("Ingrese el numero de legajo del empleado: ", "Numero de legajo invalido. Ingrese el numero de legajo del empleado: ")
    cargo=verificarInputVacio("Ingrese el cargo del empleado: ", "Ingrese un cargo valido: ")
    salarioInt=verificarNumeroInput("Ingrese el salario actual del empleado", "Salario invalido. Ingrese el salario del empleado: ")
    nombreClub=input("Ingrese el nombre del club en el que desea registrar el empleado: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea registrar el empleado: ")
        datos=verificarExistenciaClub(nombreClub)
    empleado=Empleado(nombre, apellido, sexo, edadInt, dniInt, legajoInt, cargo, salarioInt)
    clubes[datos[1]].agregarEmpleado(empleado)

def consultarEmpleados():
    nombreClub=input('Ingrese el club del que desea consultar los empleados')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los empleados: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_empleados)):
        print(clubes[datos[1]].lista_empleados[j].nombre, '\n')

def generarPago():
    montoInt=verificarNumeroInput("Ingrese el monto:", "Monto invalido. Ingrese el monto:")
    fecha=verificarInputVacio("Ingrese la fecha:", "Ingrese una fecha valida: ")
    codigoPagoInt=verificarNumeroInput("Ingrese el codigo de pago: ", "Codigo de pago invalido. Ingrese el codigo de pago: ")
    nombreClub=input("Ingrese el nombre del club en el que desea generar el pago: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea generar el pago: ")
        datos=verificarExistenciaClub(nombreClub)
    nroSocioInt=verificarNumeroInput("Ingrese el numero de socio: ", "Numero de socio invalido. Ingrese el numero de socio: ")
    pago=Pago(montoInt, fecha, nroSocioInt, codigoPagoInt)
    clubes[datos[1]].agregarPago(pago)

def eliminarPago():
    nombreClub=input("Ingrese el nombre del club en el que desea eliminar un pago: ")
    datos=verificarExistenciaClub(nombreClub)
    while(datos[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea eliminar un pago: ")
        datos=verificarExistenciaClub(nombreClub)
    nroPagoInt=verificarNumeroInput("Ingrese el numero de pago del pago que desea eliminar: ","Numero de pago invalido. Ingrese el numero de pago del pago que desea eliminar: " )
    clubes[datos[1]].eliminarPago(nroPagoInt)

def consultarPagos():
    nombreClub=input('Ingrese el club del que desea consultar los pagos')
    datos=verificarExistenciaClub(nombreClub)
    while (datos[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el club del que quiere consultar los pagos: ')
        datos=verificarExistenciaClub(nombreClub)
    for j in range(len(clubes[datos[1]].lista_pagos)):
        print(clubes[datos[1]].lista_pagos[j].monto, '\n')

def crearReserva():
    fechaReserva=verificarInputVacio("Ingrese la fecha de reserva: ", "Ingrese una fecha valida: ")
    horaReserva=verificarInputVacio("Ingrese la hora de reserva:", "Ingrese una hora valida: ")
    nroReservaInt=verificarExistenciaClub("Ingrese el numero de reserva: ", "Numero de reserva invalido. Ingrese el numero de reserva: ")
    nombreClub=input("Ingrese el nombre del club en el que desea realizar la reserva: ")
    datos1=verificarExistenciaClub(nombreClub)
    while(datos1[0]==False):
        nombreClub=input("Club inexistente. Ingrese el nombre del club en el que desea realizar la reserva: ")
        datos1=verificarExistenciaClub(nombreClub)
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea reservar: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea reservar: ")
    datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    while(datos2[0]==False):
        print("Instalacion inexistente. Ingrese el codigo de la instalacion que desea reservar: ")
        codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea reservar: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea reservar: ")
        datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    reserva=Reserva(fechaReserva, horaReserva, nroReservaInt)
    clubes[datos1[1]].lista_instalaciones[datos2[1]].agregarReserva(reserva)

def consultarReservas():
    nombreClub=input('Ingrese el nombre del club del que desea consultar las reservas de una instalacion')
    datos1=verificarExistenciaClub(nombreClub)
    while (datos1[0] == False):
        nombreClub=input('Nombre del club inexistente. Ingrese el nombre del club del que desea consultar las reservas de una instalacion: ')
        datos1=verificarExistenciaClub(nombreClub)
    codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea consultar las reservas: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
    datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    while (datos2[0] == False):
        print("Instalacion inexistente. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
        codigoInstalacionInt=verificarNumeroInput("Ingrese el codigo de la instalacion que desea consultar las reservas: ", "Codigo invalido. Ingrese el codigo de la instalacion que desea consultar las reservas: ")
        datos2=verificarExistenciaInstalacion(codigoInstalacionInt, datos1[1])
    for r in range(len(clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas)):
        print( clubes[datos1[1]].lista_instalaciones[datos2[1]].lista_reservas[r].nroReserva, '\n')

ingreso("archivo.txt")