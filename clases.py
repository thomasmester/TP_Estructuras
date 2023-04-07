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
    def __init__(self, nombre, apellido, sexo, edad, DNI, nroSocio):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.nroSocio=nroSocio

class Empleado(Persona):
    def __init__(self, nombre, apellido, sexo, edad, DNI, legajo):
        super().__init__(nombre, apellido, sexo, edad, DNI)
        self.legajo=legajo

class Actividad:
    def __init__(self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo
    def informacion(self):
        print("La actividad {} es {}".format(self.nombre, self.tipo))