class Club:
    def __init__(self, nombre, anioFundacion, direccion):
        self.nombre = nombre
        self.anioFundacion = anioFundacion
        self.direccion = direccion
        self.lista_socios = []
        self.lista_instalaciones = []

    def agregarSocio(self, socio):
        esta = False
        for i in range(len(self.lista_socios)):
            if socio.nroSocio == self.lista_socios[i].nroSocio:
                esta = True
        if esta == False:
            self.lista_socios.append(socio)
            print("El socio {} {} ha sido agregado con éxito al club.".format(socio.nombre, socio.apellido))
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
            print("El socio cuyo numero de socio es {} ha sido eliminado con éxito.".format(nroSocio))
        else:
            print("No hay ningun socio en el club cuyo numero de socio sea el {}".format(nroSocio))

    def agregarInstalacion(self, instalacion):
        esta = False
        for i in range(len(self.lista_instalaciones)):
            if instalacion.codigoInstalacion == self.lista_instalaciones[i].codigoInstalacion:
                esta = True
        if esta == False:
            self.lista_instalaciones.append(instalacion)
            print("La instalacion {} cuyo codigo es {} ha sido agregado con éxito al club.".format(instalacion.nombre, instalacion.codigoInstalacion))
        else:
            print("Ya existe una instalacion con el codigo {}".format(instalacion.codigoInstalacion))

    def eliminarInstalacion(self, codigoInstalacion):
        esta = False
        for i in range(len(self.lista_instalaciones)):
            if codigoInstalacion == self.lista_instalaciones[i].codigoInstalacion:
                esta = True
                indiceAux = i
        if esta == True:
            self.lista_instalaciones.pop(indiceAux)
            print("La instalacion cuyo codigo es {} ha sido eliminada con éxito.".format(codigoInstalacion))
        else:
            print("No hay ninguna instalacion en el club cuyo codigo sea el {}".format(codigoInstalacion))


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
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def informacion(self):
        print("La actividad {} es {}".format(self.nombre, self.tipo))

class Instalacion:
    def __init__(self, nombre, descripcion, ubicacion, horaApertura, horaCierre, codigoInstalacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
        self.codigoInstalacion=codigoInstalacion

class Reserva:
    def __init__(self, nombre, descripcion, ubicacion, horaApertura, horaCierre, codigoInstalacion, fechaReserva, horaReserva):
        super().__init__(nombre, descripcion, ubicacion, horaApertura, horaCierre, codigoInstalacion)
        self.fechaReserva = fechaReserva
        self.horaReserva = horaReserva


class Evento:
    def __init__(self, nombre, descripcion, fecha, hora):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora


class Pago:
    def __init__(self, monto, fecha, nroSocio):
        self.monto = monto
        self.fecha = fecha
        self.nroSocio = nroSocio