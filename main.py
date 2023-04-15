from .clases.Actividad import Actividad
from .clases.Club import Club
from .clases.Empleado import Empleado
from .clases.Evento import Evento
from .clases.Instalacion import Instalacion
from .clases.Pago import Pago
from .clases.Persona import Persona
from .clases.Reserva import Reserva
from .clases.Socio import Socio

def ingreso(archivo):
    archivo = open(archivo,"a",encoding="utf-8")
    print("1. Registrarse",'\n',"2. Iniciar sesión",'\n')
    opcion = input("Ingrese la opción: ")
    while opcion != 1 and opcion != 2:
        opcion = input("Ingrese la opción: ")
    if opcion == 1:
        usuario = input("Ingrese usuario: ")
        contrsenia = input("Ingrese contraseña: ")
        archivo.write(usuario + " " + contrsenia + '\n')
    else:
        lista = []
        otros = [" ",'\n']
        for linea in archivo:
            for elemento in linea:
                if elemento not in otros:
                    lista.append(elemento)
        for i in range(len(lista)):
            if lista[i] == usuario:
                return lista[i+1] == contrsenia

print("aca va a estar el programa principal")
