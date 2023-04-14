class Actividad:
    def __init__(self, nombre, tipo, codigoInstalacion):
        self.nombre = nombre
        self.tipo = tipo
        self.codigoInstalacion=codigoInstalacion
    def informacion(self):
        print("La actividad {} es {}".format(self.nombre, self.tipo))