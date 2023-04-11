class Club:
    def __init__(self, nombre, anioFundacion, direccion):
        self.nombre = nombre
        self.anioFundacion = anioFundacion
        self.direccion = direccion
        self.lista_socios = []

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
    def __init__(self, nombre, descripcion, ubicacion, horaApertura, horaCierre):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre


class Reserva:
    def __init__(self, nombre, descripcion, ubicacion, horaApertura, horaCierre, fechaReserva, horaReserva):
        super().__init__(nombre, descripcion, ubicacion, horaApertura, horaCierre)
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


c = Club('river', 912, 'iguazu 343 ')
s1 = Socio('manu', 'ebje', 'm', 16, 44333222, 1, 'manu@ejbe.com')
s2 = Socio('manu', 'ebje', 'm', 16, 44333222, 2, 'manu@ejbe.com')
s3 = Socio('manu', 'ebje', 'm', 16, 44333222, 2, 'manu@ejbe.com')
c.agregarSocio(s1)
c.agregarSocio(s2)
c.agregarSocio(s3)
c.eliminarSocio(2)
c.eliminarSocio(3)
print(c.lista_socios[0])
