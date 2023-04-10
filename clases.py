class Club:
    def __init__(self, nombre, anioFundacion, direccion):
        self.nombre=nombre
        self.anioFundacion=anioFundacion
        self.direccion=direccion

class Persona:
    def __init__(self, nombre, apellido, sexo, edad, DNI):
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.edad=edad
        self.DNI=DNI
    def presentacion(self):
        print("Me llamo {} {} y tengo {} años".format(self.nombre, self.apellido, self.edad))

class Socio(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, nroSocio, correoElectronico):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.nroSocio=nroSocio
        self.correoElectronico=correoElectronico

class Empleado(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, legajo, cargo, salario):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.legajo=legajo
        self.cargo=cargo
        self.salario=salario

class Actividad:
    def __init__(self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo
    def informacion(self):
        print("La actividad {} es {}".format(self.nombre, self.tipo))

class Instalacion:
    def __init__(self, nombre, descripcion, ubicacion, horaApertura, horaCierre):
        self.nombre=nombre
        self.descripcion=descripcion
        self.ubicacion=ubicacion
        self.horaApertura=horaApertura
        self.horaCierre=horaCierre

class Reserva:
    def __init__(self, nombre, descripcion, ubicacion, horaApertura, horaCierre, fechaReserva, horaReserva):
        super().__init__(nombre, descripcion, ubicacion, horaApertura, horaCierre)
        self.fechaReserva=fechaReserva
        self.horaReserva=horaReserva

class Evento:
    def __init__(self, nombre, descripcion, fecha, hora):
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha=fecha
        self.hora=hora

class Pago:
    def __init__(self, monto, fecha, nroSocio):
        self.monto=monto
        self.fecha=fecha
        self.nroSocio=nroSocio