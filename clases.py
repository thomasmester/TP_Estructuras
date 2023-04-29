class Club:
    lista_nombres = []
    def __init__(self, nombre, anioFundacion, direccion):
        if nombre in self.lista_nombres:
            raise ValueError("Nombre repetido")
        self.anioFundacion = anioFundacion
        self.direccion = direccion
        self.lista_socios = []
        self.lista_instalaciones = []
        self.lista_pagos=[]

    def agregarSocio(self, socio):
        esta = False
        for i in range(len(self.lista_socios)):
            if socio.nroSocio == self.lista_socios[i].nroSocio:
                esta = True
        if esta == False:
            self.lista_socios.append(socio)  
            print("El socio {} {} ha sido agregado con éxito al club.".format(
                socio.nombre, socio.apellido))
        else:
            print("Ya existe un socio con el numero de socio {}".format(socio.nroSocio))
            

    def eliminarSocio(self, nroSocio):
        esta = False
        for i in range(len(self.lista_socios)):
            if nroSocio == self.lista_socios[i].nroSocio:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_socios.pop(indiceAux)
            print("El socio cuyo numero de socio es {} ha sido eliminado con éxito.".format(
                nroSocio))
        else:
            print("No hay ningun socio en el club cuyo numero de socio sea el {}".format(
                nroSocio))
    
    def agregarPago(self,pago):
        esta = False
        for i in range(len(self.lista_pagos)):
            if pago.codigoPago == self.lista_pagos[i].codigoPago:
                esta = True
        if esta == False:
            self.lista_socios.append(pago)  
            print("El socio {} {} ha sido agregado con éxito al club.").format(
                pago.codigoPago)
        else:
            print("Ya existe un pago con el codigo de pago {}".format(pago.codigoPago))
            
    def eliminarPago(self, codigoPago):
        esta = False
        for i in range(len(self.lista_pagos)):
            if codigoPago == self.lista_pagos[i].codigoPago:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_pagos.pop(indiceAux)
            print("El pago cuyo codigo es {} ha sido eliminado con éxito.".format(
            codigoPago))
        else:
            print("No hay registrado un pago con el codigo {}".format(
                codigoPago))
               
    def agregarInstalacion(self, instalacion):
        esta = False
        for i in range(len(self.lista_instalaciones)):
            if instalacion.codigoInstalacion == self.lista_instalaciones[i].codigoInstalacion:
                esta = True
        if esta == False:
            self.lista_instalaciones.append(instalacion)
            print("La instalacion {} cuyo codigo es {} ha sido agregado con éxito al club.".format(
                instalacion.nombre, instalacion.codigoInstalacion))
        else:
            print("Ya existe una instalacion con el codigo {}".format(
                instalacion.codigoInstalacion))

    def eliminarInstalacion(self, codigoInstalacion):
        esta = False
        for i in range(len(self.lista_instalaciones)):
            if codigoInstalacion == self.lista_instalaciones[i].codigoInstalacion:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_instalaciones.pop(indiceAux)
            print("La instalacion cuyo codigo es {} ha sido eliminada con éxito.".format(
                codigoInstalacion))
        else:
            print("No hay ninguna instalacion en el club cuyo codigo sea el {}".format(
                codigoInstalacion))


class Persona:
    def __init__(self, nombre, apellido, sexo, edad, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.DNI = DNI

    def presentacion(self):
        print("Me llamo {} {} y tengo {} años".format(
            self.nombre, self.apellido, self.edad))


class Socio(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, nroSocio, correoElectronico):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.nroSocio = nroSocio
        self.correoElectronico = correoElectronico


class Empleado(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, legajo, cargo, salario):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.legajo = legajo
        self.cargo = cargo
        self.salario = salario


class Actividad:
    def __init__(self, nombre, tipo, codigoInstalacion):
        self.nombre = nombre
        self.tipo = tipo
        self.codigoInstalacion=codigoInstalacion
    def informacion(self):
        print("La actividad {} es {}".format(self.nombre, self.tipo))


class Instalacion:
    def __init__(self, nombre, descripcion, horaApertura, horaCierre, codigoInstalacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
        self.codigoInstalacion = codigoInstalacion

        self.listaReservas = []

    def agregarReserva(self, res):
        disponible = True
        for i in range(len(self.listaReservas)):
            if res.fechaReserva == self.listaReservas[i].fechaReserva and res.horaReserva == self.listaReservas[i].horaReserva:
                disponible = False
        if disponible:
            self.listaReservas.append(res)
            print('Su reserva para el día {} a las {} ha sido agendada con éxito.'.format(
                res.fechaReserva, res.horaReserva))
        else:
            print(
                'El horario de las {} en el día {} no está disponible, por favor seleccione otro.'.format(res.horaReserva, res.fechaReserva))

    def eliminarReserva(self, nroReserva):
        horaElim = ''
        fechaElim = ''
        eliminada = False
        for j in range(len(self.listaReservas)):
            if nroReserva == self.listaReservas[j].nroReserva:

                horaElim = self.listaReservas[j].horaReserva
                fechaElim = self.listaReservas[j].fechaReserva
                self.listaReservas.pop(j)
                eliminada = True
            if not eliminada:
                print('No existe una reserva con el número {}'.format(nroReserva))
            else:
                print('La reserva de las {} el día {} fue eliminada con éxito.'.format(
                    horaElim, fechaElim))


class Reserva:
    def __init__(self, fechaReserva, horaReserva, nroReserva):
        self.nroReserva = nroReserva
        self.fechaReserva = fechaReserva
        self.horaReserva = horaReserva


class Evento:
    def __init__(self, nombre, descripcion, fecha, hora, codigoInstalacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.codigoInstalacion=codigoInstalacion


class Pago:
    def __init__(self, monto, fecha, socio: Socio, club: Club,codigoPago):
        if socio not in club.lista_socios:
            raise ValueError ('El socio {} no está en el club {}'.format(socio.nombre,club.nombre))  
        self.club = club      
        self.monto = monto
        self.fecha = fecha
        self.socio=socio 
        self.codigoPago = codigoPago   
        

def ingreso(archivo):
    archivo = open(archivo,"a",encoding="utf-8")
    print("1. Registrarse",'\n',"2. Iniciar sesión",'\n')
    opcion = input("Ingrese la opción: ")
    while opcion != 1 and opcion != 2:
        opcion = input("Ingrese la opción: ")
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