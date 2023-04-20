class Club:
    lista_nombres = []

    def __init__(self, nombre, anioFundacion, direccion):
        if nombre in self.lista_nombres:
            raise ValueError("Nombre repetido")
        self.lista_nombres.append(nombre)
        self.nombre = nombre
        self.anioFundacion = anioFundacion
        self.direccion = direccion
        self.lista_socios = []
        self.lista_instalaciones = []
        self.lista_pagos = []

    def guardarClub(self):
        socios_text = ""
        inst_text = ""
        pagos_text = ""
        for socio in self.lista_socios:
            socios_text += (socio.nombre + "," + socio.apellido + "," + socio.sexo + "," + socio.edad + "," +
                            socio.DNI + "," + str(socio.nroSocio) + "," + socio.correoElectronico + '\n')
        for inst in self.lista_instalaciones:
            inst_text += (inst.nombre + "," + inst.descripcion + "," + inst.horaApertura + "," + inst.horaCierre + "," +
                          inst.codigoInstalacion + '\n')
        for pago in self.lista_pagos:
            pagos_text += (pago.monto + "," + pago.fecha + "," +
                           str(pago.socio.nroSocio) + "," + pago.codigoPago + '\n')

        total_text = (socios_text + '@' + '\n' +
                      inst_text + '@' + '\n' + pagos_text)
        with open("{}.txt".format(self.nombre), "w") as f:
            f.write(total_text)

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

    def agregarPago(self, pago):
        esta = False
        for i in range(len(self.lista_pagos)):
            if pago.codigoPago == self.lista_pagos[i].codigoPago:
                esta = True
        if esta == False:
            self.lista_pagos.append(pago)
            print("El pago {} ha sido agregado con éxito al club.".format(
                pago.codigoPago))
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
