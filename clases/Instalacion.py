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
            print('Su reserva para el día {} a las {} a sido agendada con éxito.'.format(
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