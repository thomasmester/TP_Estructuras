class Persona:
    def __init__(self, nombre, apellido, sexo, edad, DNI):
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.edad=edad
        self.DNI=DNI

class Socio(Persona):
    def __init__(self, nombre, apellido, sexo, edad, nroSocio):
        super().__init__(nombre, apellido, sexo, edad)
        self.nroSocio=nroSocio