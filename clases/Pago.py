from clases.Socio import Socio
from clases.Club import Club


class Pago:
    def __init__(self, monto, fecha, socio: Socio, club: Club, codigoPago):
        if socio not in club.lista_socios:
            raise ValueError('El socio {} no está en el club {}'.format(
                socio.nombre, club.nombre))
        self.monto = monto
        self.fecha = fecha
        self.socio = socio
        self.codigoPago = codigoPago
