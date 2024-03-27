from operaciones import Operaciones

def menu():

    print("Escoja la tarea que desea realizar:")
    print("\n1)Suma\n2)Resta\n3)Producto\n4)Division\n")
    op = int(input("Ingrese su opcion: "))

    while op < 1 or op > 4:
        print("Errod de digitacion.")
        print("Escoja la tarea que desea realizar:")
        print("\n1)Suma\n2)Resta\n3)Producto\n4)Division\n")
        op = int(input("Ingrese su opcion: "))

    if op == 1:
        v1 = int(input("Ingrese su primer número: "))
        v2 = int(input("Ingrese su segundo número: "))
        accion1 = Operaciones(n1=v1, n2=v2)
        print(accion1.suma())

    if op == 2:
        v1 = int(input("Ingrese su primer número: "))
        v2 = int(input("Ingrese su segundo número: "))
        accion2 = Operaciones(n1=v1, n2=v2)
        print(accion2.resta())

    if op == 3:
        v1 = int(input("Ingrese su primer número: "))
        v2 = int(input("Ingrese su segundo número: "))
        accion3 = Operaciones(n1=v1, n2=v2)
        print(accion3.producto())

    if op == 4:
        v1 = int(input("Ingrese su primer número: "))
        v2 = int(input("Ingrese su segundo número: "))
        accion4 = Operaciones(n1=v1, n2=v2)
        print(accion4.division())


while True:
    op2 = str(input("Presione 'M' para desplegar el menu o 'F' para finalizar:"))
    if op2 == 'M' or op2 == 'm':
        menu()
    if op2 == 'F' or op2 == 'f':
        break
