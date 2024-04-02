from operaciones import Operaciones
from pruebas import *

#Solicitud de datos a operar
print("Por favor ingrese los valores a operar: ")
v1 = int(input("Ingrese el primer termino: "))
v2 = int(input("Ingrese el segundo termino: "))
#Se pasan los parametros al constructor y parametrización de la clase "operaciones".
term_aop = Operaciones(n1=v1, n2=v2)

#Siclo Do-while para realizar varias tarear con los mimos operandos ingresados
while True:
    op2 = str(input("Presione 'M' para desplegar el menu o 'F' para finalizar:"))
    if op2 == 'M' or op2 == 'm':
        print("Escoja la tarea que desea realizar:")
        print("\n1)Suma\n2)Resta\n3)Producto\n4)Division\n")
        op = str(input(f"Ingrese su opcion: "))

        #Se llamo a el metodo "ejecutar" de la clase "Operaciones".
        ej = term_aop.ejecutar(tipo=op)
        print(ej)

    if op2 == 'F' or op2 == 'f':
        break