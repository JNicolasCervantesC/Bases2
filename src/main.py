from operaciones import Operaciones


val1 = int(input("Ingresu su primer número: "))
val2 = int(input("Ingrese su segundo número: "))

#Creación del objeto de la clase tipo "Sumas"
operadores = Operaciones(n1=val1, n2=val2)


total1 = operadores.suma()
total2 = operadores.resta()
total3 = operadores.producto()
total4 = operadores.cociente()

print("[Suma: ", total1,"; Resta: ", total2,"; Producto: ", total3,"; Cociente: ", total4, "]")


#que es el init en una clase:
#Constructor que me permite acceder a los atributos de la Clase.

#agregar init a esta clase:
#Completado.

#que es "self"
#palabra reservada del contrucotor para referirse a un atributo de esa clase.

#como compartir rama
#commentarios